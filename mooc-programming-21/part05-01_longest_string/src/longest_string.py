def longest(strings: list):
    newlist = []
    for word in strings:
        newlist.append(len(word))
    index = newlist.index(max(newlist))
    return strings[index]