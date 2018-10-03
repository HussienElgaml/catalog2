 #!/usr/bin/python
from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories,Courses
from sqlalchemy.pool import SingletonThreadPool
from sqlalchemy.orm import scoped_session

from flask import session as login_session
import random
import string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Restaurant Menu Application"



engine = create_engine('postgresql://catalog:password@localhost/catalog')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = scoped_session(DBSession)



@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)

@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response



@app.route('/categories/<int:category_id>/courses/JSON')
def coursesJSON(category_id):
   courses=session.query(Courses).filter_by(category_id=category_id).all()
   return jsonify(Menu_Item=Menu_Item.serialize)


@app.route('/JSON')
@app.route('/categories/JSON')
def categoriesJSON():
    categories = session.query(Categories).all()
    courses=session.query(Courses).all()
    return jsonify(categories=[r.serialize for r in categories])


@app.route('/')
@app.route('/categories/')
def show_categories():
	categories = session.query(Categories).all()
	courses=session.query(Courses).all()
	return render_template('categories.html', categories=categories,courses=courses)
	
@app.route('/categories/new/', methods=['GET', 'POST'])
def new_category():
	if request.method == 'POST':
		new_category=Categories(name=request.form['name'])
		session.add(new_category)
		session.commit()
		return redirect(url_for('show_categories'))
	else:
		return render_template('new_category.html')
	
@app.route('/categories/<int:category_id>/edit/', methods=['GET', 'POST'])
def edit_category(category_id):
	edited_category = session.query(Categories).filter_by(id=category_id).one()
	if request.method == 'POST':
		if request.form['name']:
			edited_category.name=request.form['name']
			session.add(edited_category)
			session.commit()
			return redirect(url_for('show_categories'))
	else:
		return render_template('edit_category.html', category=edited_category)
	
@app.route('/categories/<int:category_id>/delete/', methods=['GET', 'POST'])
def delete_category(category_id):
	deleted_category = session.query(Categories).filter_by(id=category_id).one()
	if request.method == 'POST':
		session.delete(deleted_category)
		session.commit()
		return redirect(url_for('show_categories'))
	else:
		return render_template('delete_category.html', category=deleted_category)	


@app.route('/categories/<int:category_id>/courses/')
def show_courses(category_id):
	categories = session.query(Categories).all()
	courses=session.query(Courses).filter_by(category_id=category_id).all()
	return render_template('show_courses.html', courses=courses, categories=categories,category_id=category_id)


@app.route('/categories/<int:category_id>/courses/new', methods=['GET', 'POST'])
def new_course(category_id):
	if request.method == 'POST':
		new_course = Courses(name=request.form['name'], description=request.form[
						'description'], link=request.form['link'],photo_url=request.form['photo_url'], category_id=category_id)
		session.add(new_course)
		session.commit()

		return redirect(url_for('show_courses', category_id=category_id))
	else:
		return render_template('new_course.html', category_id=category_id)

@app.route('/categories/<int:category_id>/courses/<int:course_id>/edit/', methods=['GET', 'POST'])
def edit_course(category_id, course_id):
	edited_course=session.query(Courses).filter_by(id=course_id).one()
	if request.method == 'POST':
		if request.form['name']:
			edited_course.name = request.form['name']
		if request.form['description']:
			edited_course.description = request.form['description']
		if request.form['link']:
			edited_course.link = request.form['link']
		if request.form['photo_url']:
			edited_course.photo_url = request.form['photo_url']
			
		session.add(edited_course)
		session.commit()
		return redirect(url_for('show_courses', category_id=category_id))
	else:

		return render_template(
			'edit_course.html', category_id=category_id, course_id=course_id, course=edited_course)
	
@app.route('/categories/<int:category_id>/courses/<int:course_id>/delete/', methods=['GET', 'POST'])
def delete_course(category_id, course_id):
	deleted_course=session.query(Courses).filter_by(id=course_id).one()
	if request.method == 'POST':
		session.delete(deleted_course)
		session.commit()
		return redirect(url_for('show_courses', category_id=category_id))
	else:
		return render_template('delete_course.html',category_id=category_id,course=deleted_course)

@app.route('/categories/<int:category_id>/courses/<int:course_id>')
def course_details(category_id, course_id):
	course=session.query(Courses).filter_by(id=course_id).one()
	return render_template('course_details.html', category_id=category_id, course_id=course_id,course=course)


if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
