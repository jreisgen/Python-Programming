def formatted(mylist):
    newlist = []
    for i in mylist:
        newi = f"{i:.2f}"
        newlist.append(newi)
    return newlist
if __name__ == "__main__":
    mylist1 = [1.2323, 4.131232, 4.1231]
    newlist1 = formatted(mylist1)
    print(newlist1)
