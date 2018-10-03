from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Categories, Base, Courses

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Menu for UrbanBurger
category1 = Categories(name="Urban Burger")

session.add(category1)
session.commit()

Courses2 = Courses(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     link="$7.50", photo_url="Entree", category=category1)

session.add(Courses2)
session.commit()


Courses1 = Courses(name="French Fries", description="with garlic and parmesan",
                     link="$2.99", photo_url="Appetizer", category=category1)

session.add(Courses1)
session.commit()

Courses2 = Courses(name="Chicken Burger", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                     link="$5.50", photo_url="Entree", category=category1)

session.add(Courses2)
session.commit()

Courses3 = Courses(name="Chocolate Cake", description="fresh baked and served with ice cream",
                     link="$3.99", photo_url="Dessert", category=category1)

session.add(Courses3)
session.commit()

Courses4 = Courses(name="Sirloin Burger", description="Made with grade A beef",
                     link="$7.99", photo_url="Entree", category=category1)

session.add(Courses4)
session.commit()

Courses5 = Courses(name="Root Beer", description="16oz of refreshing goodness",
                     link="$1.99", photo_url="Beverage", category=category1)

session.add(Courses5)
session.commit()

Courses6 = Courses(name="Iced Tea", description="with Lemon",
                     link="$.99", photo_url="Beverage", category=category1)

session.add(Courses6)
session.commit()

Courses7 = Courses(name="Grilled Cheese Sandwich", description="On texas toast with American Cheese",
                     link="$3.49", photo_url="Entree", category=category1)

session.add(Courses7)
session.commit()

Courses8 = Courses(name="Veggie Burger", description="Made with freshest of ingredients and home grown spices",
                     link="$5.99", photo_url="Entree", category=category1)

session.add(Courses8)
session.commit()


# Menu for Super Stir Fry
category2 = Categories(name="Super Stir Fry")

session.add(category2)
session.commit()


Courses1 = Courses(name="Chicken Stir Fry", description="With your choice of noodles vegetables and sauces",
                     link="$7.99", photo_url="Entree", category=category2)

session.add(Courses1)
session.commit()

Courses2 = Courses(
    name="Peking Duck", description=" A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", link="$25", photo_url="Entree", category=category2)

session.add(Courses2)
session.commit()

Courses3 = Courses(name="Spicy Tuna Roll", description="Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ",
                     link="15", photo_url="Entree", category=category2)

session.add(Courses3)
session.commit()

Courses4 = Courses(name="Nepali Momo ", description="Steamed dumplings made with vegetables, spices and meat. ",
                     link="12", photo_url="Entree", category=category2)

session.add(Courses4)
session.commit()

Courses5 = Courses(name="Beef Noodle Soup", description="A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.",
                     link="14", photo_url="Entree", category=category2)

session.add(Courses5)
session.commit()

Courses6 = Courses(name="Ramen", description="a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.",
                     link="12", photo_url="Entree", category=category2)

session.add(Courses6)
session.commit()


# Menu for Panda Garden
category1 = Categories(name="Panda Garden")

session.add(category1)
session.commit()


Courses1 = Courses(name="Pho", description="a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.",
                     link="$8.99", photo_url="Entree", category=category1)

session.add(Courses1)
session.commit()

Courses2 = Courses(name="Chinese Dumplings", description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.",
                     link="$6.99", photo_url="Appetizer", category=category1)

session.add(Courses2)
session.commit()

Courses3 = Courses(name="Gyoza", description="The most prominent differences between Japanese-style gyoza and Chinese-style jiaozi are the rich garlic flavor, which is less noticeable in the Chinese version, the light seasoning of Japanese gyoza with salt and soy sauce, and the fact that gyoza wrappers are much thinner",
                     link="$9.95", photo_url="Entree", category=category1)

session.add(Courses3)
session.commit()

Courses4 = Courses(name="Stinky Tofu", description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
                     link="$6.99", photo_url="Entree", category=category1)

session.add(Courses4)
session.commit()

Courses2 = Courses(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     link="$9.50", photo_url="Entree", category=category1)

session.add(Courses2)
session.commit()


# Menu for Thyme for that
category1 = Categories(name="Thyme for That Vegetarian Cuisine ")

session.add(category1)
session.commit()


Courses1 = Courses(name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
                     link="$2.99", photo_url="Dessert", category=category1)

session.add(Courses1)
session.commit()

Courses2 = Courses(name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto",
                     link="$5.99", photo_url="Entree", category=category1)

session.add(Courses2)
session.commit()

Courses3 = Courses(name="Honey Boba Shaved Snow", description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi",
                     link="$4.50", photo_url="Dessert", category=category1)

session.add(Courses3)
session.commit()

Courses4 = Courses(name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",
                     link="$6.95", photo_url="Appetizer", category=category1)

session.add(Courses4)
session.commit()

Courses5 = Courses(name="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
                     link="$7.95", photo_url="Entree", category=category1)

session.add(Courses5)
session.commit()

Courses2 = Courses(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     link="$6.80", photo_url="Entree", category=category1)

session.add(Courses2)
session.commit()


# Menu for Tony's Bistro
category1 = Categories(name="Tony\'s Bistro ")

session.add(category1)
session.commit()


Courses1 = Courses(name="Shellfish Tower", description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",
                     link="$13.95", photo_url="Entree", category=category1)

session.add(Courses1)
session.commit()

Courses2 = Courses(name="Chicken and Rice", description="Chicken... and rice",
                     link="$4.95", photo_url="Entree", category=category1)

session.add(Courses2)
session.commit()

Courses3 = Courses(name="Mom's Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom",
                     link="$6.95", photo_url="Entree", category=category1)

session.add(Courses3)
session.commit()

Courses4 = Courses(name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
                     description="Milk, cream, salt, ..., Liquid nitrogen magic", link="$3.95", photo_url="Dessert", category=category1)

session.add(Courses4)
session.commit()

Courses5 = Courses(name="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth with a soft-boiled egg",
                     link="$7.95", photo_url="Entree", category=category1)

session.add(Courses5)
session.commit()


# Menu for Andala's
category1 = Categories(name="Andala\'s")

session.add(category1)
session.commit()


Courses1 = Courses(name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
                     link="$9.95", photo_url="Entree", category=category1)

session.add(Courses1)
session.commit()

Courses2 = Courses(name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",
                     link="$7.95", photo_url="Entree", category=category1)

session.add(Courses2)
session.commit()

Courses3 = Courses(name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
                     link="$6.50", photo_url="Appetizer", category=category1)

session.add(Courses3)
session.commit()

Courses4 = Courses(name="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
                     link="$6.75", photo_url="Appetizer", category=category1)

session.add(Courses4)
session.commit()

Courses2 = Courses(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     link="$7.00", photo_url="Entree", category=category1)

session.add(Courses2)
session.commit()


# Menu for Auntie Ann's
category1 = Categories(name="Auntie Ann\'s Diner' ")

session.add(category1)
session.commit()

Courses9 = Courses(name="Chicken Fried Steak", description="Fresh battered sirloin steak fried and smothered with cream gravy",
                     link="$8.99", photo_url="Entree", category=category1)

session.add(Courses9)
session.commit()


Courses1 = Courses(name="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
                     link="$2.99", photo_url="Dessert", category=category1)

session.add(Courses1)
session.commit()

Courses2 = Courses(name="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
                     link="$10.95", photo_url="Entree", category=category1)

session.add(Courses2)
session.commit()

Courses3 = Courses(name="Morels on toast (seasonal)", description="Wild morel mushrooms fried in butter, served on herbed toast slices",
                     link="$7.50", photo_url="Appetizer", category=category1)

session.add(Courses3)
session.commit()

Courses4 = Courses(name="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",
                     link="$8.95", photo_url="Entree", category=category1)

session.add(Courses4)
session.commit()

Courses2 = Courses(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     link="$9.50", photo_url="Entree", category=category1)

session.add(Courses2)
session.commit()

Courses10 = Courses(name="Spinach Ice Cream", description="vanilla ice cream made with organic spinach leaves",
                      link="$1.99", photo_url="Dessert", category=category1)

session.add(Courses10)
session.commit()


# Menu for Cocina Y Amor
category1 = Categories(name="Cocina Y Amor ")

session.add(category1)
session.commit()


Courses1 = Courses(name="Super Burrito Al Pastor", description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla",
                     link="$5.95", photo_url="Entree", category=category1)

session.add(Courses1)
session.commit()

Courses2 = Courses(name="Cachapa", description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
                     link="$7.99", photo_url="Entree", category=category1)

session.add(Courses2)
session.commit()


category1 = Categories(name="State Bird Provisions")
session.add(category1)
session.commit()

Courses1 = Courses(name="Chantrelle Toast", description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",
                     link="$5.95", photo_url="Appetizer", category=category1)

session.add(Courses1)
session.commit

Courses1 = Courses(name="Guanciale Chawanmushi", description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)",
                     link="$6.95", photo_url="Dessert", category=category1)

session.add(Courses1)
session.commit()


Courses1 = Courses(name="Lemon Curd Ice Cream Sandwich", description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews",
                     link="$4.25", photo_url="Dessert", category=category1)

session.add(Courses1)
session.commit()


print "added menu items!"
