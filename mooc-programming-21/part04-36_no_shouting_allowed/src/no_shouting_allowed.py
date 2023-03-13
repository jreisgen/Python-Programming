def no_shouting(mylist):
    newlist = []
    for i in mylist:
        if i.isupper() == False:
            newlist.append(i)
    return newlist
