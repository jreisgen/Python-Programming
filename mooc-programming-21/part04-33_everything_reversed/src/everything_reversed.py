def everything_reversed(mylist):
    newlist = []
    for i in mylist:
        string = i[::-1]
        newlist.append(string)
    newlist.reverse()
    return newlist
    


if __name__=="__main__":
    mylist = ["heye", "nosjaofes", "joasjdg"]
    print(everything_reversed(mylist))