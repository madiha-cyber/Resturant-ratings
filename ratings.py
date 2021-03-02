"""Restaurant rating lister."""

# pseudocode:
# 
# read the ratings in from the file
# store them in a dictionary
# print out the ratings in alphabetically order by restaurant
# print all of the ratings in alphabetical order, including the new ones


def display_ratings(file_name):
    """This function sorts and prints the ratings from a file"""
    the_file = open(file_name)
    restaurant_ratings = {} # dictionary
    for line in the_file:
        tokens = line.split(':')
        tokens[1] = tokens[1].strip()
        restaurant_ratings[tokens[0]] = tokens[1]

    # prompt user for new restaurant name
    new_restaurant = input('Please enter the restaurant name > ')
    new_restaurant = new_restaurant.title()
    # prompt user for new restaurant's score
    new_rating = input('Please enter the restaurant rating > ')
    # store new restaurant and rating in the dictionary
    restaurant_ratings[new_restaurant] = new_rating

    # sorted_ratings is a list of keys (restaurants)
    sorted_ratings = sorted(restaurant_ratings)
 
    for restaurant in sorted_ratings: # iterate over alphabetized keys
        print(f'{restaurant} is rated {restaurant_ratings[restaurant]}.')

    return restaurant_ratings   




    




display_ratings('scores.txt')



