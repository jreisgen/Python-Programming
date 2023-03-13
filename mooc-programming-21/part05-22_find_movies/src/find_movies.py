def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    newDictionary = {}
    newDictionary["name"] = name
    newDictionary["director"] = director
    newDictionary["year"] = year
    newDictionary["runtime"] = runtime
    database.append(newDictionary)

def find_movies(database: list, search_term: str):
    return[element for element in database if search_term in element["name"].lower()]
