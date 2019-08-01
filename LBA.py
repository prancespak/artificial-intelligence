##THE KB

KB = """
% Restaurants and their attributes
pick_restaurant(saigon) :- cuisine(Cuisine), cuisine_type(Cuisine, [vietnamese, vegetarian]), price(Price), price_range(Price, low), distance(Distance), max_distance(Distance,1), rating(Rating), rating_at_least(Rating, 4).
pick_restaurant(fasongsong) :- cuisine(Cuisine), cuisine_type(Cuisine, [korean, vegetarian]), price(Price), price_range(Price, medium), distance(Distance), max_distance(Distance, 1), rating(Rating), rating_at_least(Rating, 4).
pick_restaurant(chori) :- cuisine(Cuisine), cuisine_type(Cuisine, [argentinian]), price(Price), price_range(Price, low), distance(Distance), max_distance(Distance, 5), rating(Rating), rating_at_least(Rating, 3).
pick_restaurant(cafe_ditali) :- cuisine(Cuisine), cuisine_type(Cuisine, [italian, argentinian]), price(Price), price_range(Price, low), distance(Distance), max_distance(Distance, 1), rating(Rating), rating_at_least(Rating, 1).
pick_restaurant(hong_kong_style) :- cuisine(Cuisine), cuisine_type(Cuisine, [chinese]), price(Price), price_range(Price, medium), distance(Distance), max_distance(Distance, 9), rating(Rating), rating_at_least(Rating, 2).
pick_restaurant(cabaña) :- cuisine(Cuisine), cuisine_type(Cuisine, [argentinian]), price(Price), price_range(Price, high), distance(Distance), max_distance(Distance, 2), rating(Rating), rating_at_least(Rating, 4).
pick_restaurant(empanairo) :- cuisine(Cuisine), cuisine_type(Cuisine, [argentinian]), price(Price), price_range(Price, low), distance(Distance), max_distance(Distance, 1), rating(Rating), rating_at_least(Rating, 3).
pick_restaurant(artemisia) :- cuisine(Cuisine), cuisine_type(Cuisine, [european, vegan]), price(Price), price_range(Price, medium), distance(Distance), max_distance(Distance, 6), rating(Rating), rating_at_least(Rating, 3).
pick_restaurant(mcdonalds) :- cuisine(Cuisine), cuisine_type(Cuisine, [fastfood]), price(Price), price_range(Price, low), distance(Distance), max_distance(Distance, 1), rating(Rating), rating_at_least(Rating, 1).
pick_restaurant(biwon) :- cuisine(Cuisine), cuisine_type(Cuisine, [korean]), price(Price), price_range(Price, medium), distance(Distance), max_distance(Distance, 2), rating(Rating), rating_at_least(Rating, 2).
pick_restaurant(burger_king) :- cuisine(Cuisine), cuisine_type(Cuisine, [fastfood]), price(Price), price_range(Price, low), distance(Distance), max_distance(Distance, 3), rating(Rating), rating_at_least(Rating, 1).
pick_restaurant(la_parolaccia_trattoria) :- cuisine(Cuisine), cuisine_type(Cuisine, [italian]), price(Price), price_range(Price, high), distance(Distance), max_distance(Distance, 2), rating(Rating), rating_at_least(Rating, 3).
pick_restaurant(baifu) :- cuisine(Cuisine), cuisine_type(Cuisine, [chinese]), price(Price), price_range(Price, medium), distance(Distance), max_distance(Distance, 6), rating(Rating), rating_at_least(Rating, 1).
pick_restaurant(loving_hut) :- cuisine(Cuisine), cuisine_type(Cuisine, [vegan]), price(Price), price_range(Price, medium), distance(Distance), max_distance(Distance, 5), rating(Rating), rating_at_least(Rating, 3).
% Rules
cuisine_type([Xh|Xt], Y) :- member(Xh,Y); cuisine_type(Xt, Y).
price_range(X, Y) :- X == Y.
max_distance(X, Y) :- Y =< X.
rating_at_least(X, Y) :- X =< Y.
"""

with open("KB.pl", "w") as text_file:
    text_file.write(KB)
    
## PYTHON CODE

def get_user_input():
    """This function asks the user for input about their cuisine, price, rating and distance preferences. When the user gives false input (e.g. text instead of a number) it returns an error and the user needs to start over again. At each step, it checks whether options are available for the user. It returns the user input, or its translation to the respective values (e.g. '1' is Vietnamese)."""
    
    # USER CUISINE
    user_cuisine_int = raw_input("What type of food do you feel like? Type the number of your preferred cuisine. 1-Vietnamese, 2-Vegetarian, 3-Korean, 4-Italian, 5-Argentinian, 6-Chinese, 7-European, 8-Fast Food, 9-Vegan")
    try:
        # check for exit scenario
        if user_cuisine_int == "exit": return None, None, None, None
        # check that the input is a valid option
        if int(user_cuisine_int) not in [1,2,3,4,5,6,7,8,9]:
            print("Please enter a number between 1-9.")
            return get_user_input()
    except ValueError:
        # exception if the input is not an integer
        print("Please enter a valid integer, e.g. 1 for Vietnamese food.")
        return get_user_input()
    cuisine_dict = {"1":"vietnamese", "2":"vegetarian", "3":"korean", "4":"italian","5":"argentinian","6":"chinese","7":"european","8":"fastfood","9":"vegan"}
    user_cuisine = cuisine_dict[user_cuisine_int]

    # USER PRICE
    user_price_int = raw_input("What is your price range? Type the number of your price range. 1-low, 2-medium, 3-high")
    try:
        # check for exit scenario
        if user_price_int == "exit": return None, None, None, None
        # check that the input is a valid option
        if int(user_price_int) not in [1,2,3]:
            print("Please enter a number between 1-3.")
            return get_user_input()
    except ValueError:
        # exception if the input is not an integer
        print("Please enter a valid integer, e.g. 1 for low price.")
        return get_user_input()
    price_dict = {"1":"low", "2":"medium", "3":"high"}
    user_price = price_dict[user_price_int]

    # check temporary requirements with minimum requirements for other variables
    temp = query_KB(user_cuisine, user_price, 1, 9)
    if not temp:
        print("Please choose another combination. Unfortunately, this food is not available at this price. ")
        return get_user_input()
    else:
        print("Here are the potential options so far: {}".format((', '.join(temp))))

    
    # USER RATING
    user_rating = raw_input("How good does the food have to be, at minimum? Type the number of your preference. 1-okay, 2-decent, 3-good, 4-delicious")
    try:
        # check for exit scenario
        if user_rating == "exit": return None, None, None, None
        # check that the input is a valid option
        if int(user_rating) not in [1,2,3,4]:
            print("Please enter a number between 1-4.")
            return get_user_input()
    except ValueError:
        # exception if the input is not an integer
        print("Please enter a valid integer, e.g. 1 for okay.")
        return get_user_input()
    
     # check temporary requirements with minimum requiremets for other variable
    temp = query_KB(user_cuisine, user_price, user_rating, 9)
    if not temp:
        print("Please choose another combination. Unfortunately, this food is not available at this price and rating. ")
        return get_user_input()
    else:
        print("Here are the potential options so far: {}".format((', '.join(temp))))
    
    # USER DISTANCE
    user_distance = raw_input("What should be the maximum distance (km) of the restaurant? Round to the nearest integer.")
    
    # check that the input is an integer
    if not int(user_distance):
        print("Please enter a number.")
        return get_user_input()

    return user_cuisine, user_price, user_rating, user_distance


def query_KB(user_cuisine, user_price, user_rating, user_distance):
    """Adsd the user input to the knowledge base, query the solution, removes the facts from knowledge base and return the solution set of restaurants that fulfill user's preferences."""
    
    # assert (add) the user input to the knowledge base
    prolog.asserta("cuisine(" + str([user_cuisine]) + ")")
    prolog.asserta("price(" + str(user_price) + ")")
    prolog.asserta("rating(" + str(user_rating) + ")")
    prolog.asserta("distance(" + str(user_distance) + ")")

    # ensure solution uniqueness by defining a set
    solution_set = set()
    for solution in prolog.query("pick_restaurant(X)."):
        solution_set.add(solution.get("X", ""))

    # retract (remove) all facts from the database
    call(retractall(cuisine))
    call(retractall(price))
    call(retractall(rating))
    call(retractall(distance))

    return solution_set
  
from pyswip.prolog import Prolog
from pyswip.easy import *

prolog = Prolog() # global handle to interpreter

cuisine = Functor("cuisine",1)
price = Functor("price",1)
rating = Functor("rating",1)
distance = Functor("distance",1)
retractall = Functor("retractall")

def main():
    prolog.consult("KB.pl") # open the KB
    pick_restaurant = Functor("pick_restaurant",1)
    prolog.dynamic("cuisine/1")
    prolog.dynamic("price/1")
    prolog.dynamic("rating/1")
    prolog.dynamic("distance/1")


    # get user's preferences via user input
    print("To exit the expert system, type 'exit'.")
    user_cuisine, user_price, user_rating, user_distance = get_user_input()

    restaurant_choice = query_KB(user_cuisine, user_price, user_rating, user_distance)

    if restaurant_choice:
        if len(restaurant_choice) == 1:
            print("We recommend the following restaurant:")
        else:
            print("We recommend the following restaurants:")
        for element in restaurant_choice:
               print(element)
    else:
        print("We're sorry! It looks like there are no restaurants available with these requirements.")

# to test
main() # 7,2,3,10
