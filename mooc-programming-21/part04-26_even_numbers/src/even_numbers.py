def even_numbers(mylist):
    newlist=[]
    for i in mylist:
        if i % 2 == 0:
            newlist.append(i)
    return newlist