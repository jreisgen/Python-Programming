mylist = [1,2,3,4,5]
while True:
    index = int(input("Index:"))
    if index == -1:
        break
    else:
        newValue = int(input("New value: "))
        mylist[index] = newValue
    print(mylist)
