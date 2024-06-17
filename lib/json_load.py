from urllib.request import urlopen
import json

# == INSTRUCTIONS ==
#
# Below, you'll find lots of incomplete functions.
#
# Your job: Implement each function so that it does its job effectively.
#
# * Use the material, Python Docs and Google as much as you want

# == EXERCISES ==

# Purpose: Use Python libraries to request the provided URL, convert the
#          response data to JSON, and return the data.
# Example:
#   Call:    load_data_from_url("https://example.org/my.json")
#   Returns: A JSON object
def load_data_from_url(url):
    url = urlopen(url)
    response = url.read().decode('UTF-8')
    json_data = json.loads(response)
    return json_data

# Purpose: Use Python libraries to open the specified file, convert the
#          data to JSON, and return the data.
# Example:
#   Call:    load_data_from_file("my_test_data.json")
#   Returns: A JSON object
def load_data_from_file(filename):
    f = open(filename)
    json_data = json.load(f)
    f.close()
    return json_data

# Purpose: Load the sample JSON from file, and returns a list of films 
#           directed by the named person.
# Example:
#   Call:    get_films_by_director("my_test_data.json", "Olivia Wilde")
#   Returns: ["Booksmart, "Don't Worry Darling"]
def get_films_by_director(filename, director):
    json_data = load_data_from_file(filename)
    lst = []
    for film in json_data:
        if film["director"] == director:
            lst.append(film["name"])
    return lst

# Purpose: Load the sample JSON from file, and returns a list of films 
#           starring the named person.
# Example:
#   Call:    get_films_by_actor("my_test_data.json", "Dwayne Johnson")
#   Returns: ["Jumanji", "Jungle Cruise"]
def get_films_by_actor(filename, desired_actor):
    json_data = load_data_from_file(filename)
    lst = []
    for film in json_data:
        if desired_actor in film["stars"]:
            lst.append(film["name"])
    return lst

# Purpose: Load the sample JSON from file, and returns a list of films 
#           with a rating which is AT LEAST the value specified.
# Example:
#   Call:    get_films_with_minimum_rating("test.json", 9.3)
#   Returns: ["The Shawshank Redemption"]
def get_films_with_minimum_rating(filename, rating):
    json_data = load_data_from_file(filename)
    lst = []
    for film in json_data:
        if film["imdb_rating"] >= rating:
            lst.append(film["name"])
    return lst 

# Purpose: Load the sample JSON from file, and returns a list of films 
#           which were released during the specified years.
# Example:
#   Call:    get_films_within_year_range("my_test_data.json", 1994, 1996)
#   Returns: ["The Lion King", "Independence Day"]
def get_films_within_year_range(filename, start_year, end_year):
    json_data = load_data_from_file(filename)
    lst = []
    for film in json_data:
        if film["year"] in range(start_year, end_year):
            lst.append(film["name"])
    return lst 

# Purpose: Load the sample JSON from file, and returns a list of films 
#           in order of the year that they were released.
# Example:
#   Call:    order_films_chronologically("test.json")
#   Returns: ["12 Angry Men", "The Godfather", "The Godfather: Part II", ... ]
def order_films_chronologically(filename):
    json_data = load_data_from_file(filename)
    lst = []
    for dict in sorted(json_data, key=lambda x: x["year"]):
        lst.append(dict["name"])
    return lst

# Purpose: Load the sample JSON from file, and returns a list of films 
#           starting with the most recent.
# Example:
#   Call:    order_films_most_recent_first("test.json")
#   Returns: ["The Dark Knight", "The Shawshank Redemption", "The Godfather: Part II", ... ]
def order_films_most_recent_first(filename):
    json_data = load_data_from_file(filename)
    lst = []
    for dict in sorted(json_data, key=lambda x: x["year"], reverse=True):
        lst.append(dict["name"])
    return lst

# Purpose: Load the sample JSON from file, and returns a deduplicated list 
#           of all the actors whose name begins with that letter,
#           in alphabetical order.
# Example:
#   Call:    all_actors_starting_with_letter("test.json", "a")
#   Returns: ["Aaron Eckhart, "Al Pacino"]
def all_actors_starting_with_letter(filename, letter):
    json_data = load_data_from_file(filename)
    lst = []
    for dict in json_data:
        for actor in dict["stars"]:
            if actor[0] in (letter.upper(), letter.lower()):
                if not actor in lst:
                    lst.append(actor)
    return sorted(lst)