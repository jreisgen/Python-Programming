def oldest_person(people: list):
    newlist = []
    for item in people:
        newlist.append(item[1])
    maxi = min(newlist)
    index = newlist.index(maxi)
    return people[index][0]

if __name__ == "__main__":
    people = [("Henry", 1992), ("Hey", 1999)]
    print(oldest_person(people))
