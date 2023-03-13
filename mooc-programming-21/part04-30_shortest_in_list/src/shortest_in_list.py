def shortest(mylist):
    newlist = []
    for i in mylist:
        newlist.append(len(i))
    short = min(newlist)
    index = newlist.index(short)
    return mylist[index]