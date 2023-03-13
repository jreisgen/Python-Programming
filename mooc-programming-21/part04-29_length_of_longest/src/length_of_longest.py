def length_of_longest(mylist):
    newlist = []
    for i in mylist:
        newlist.append(len(i))
    return max(newlist)
    