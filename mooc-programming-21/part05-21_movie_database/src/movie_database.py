def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    newDictionary = {}
    newDictionary["name"] = name
    newDictionary["director"] = director
    newDictionary["year"] = year
    newDictionary["runtime"] = runtime
    database.append(newDictionary)


