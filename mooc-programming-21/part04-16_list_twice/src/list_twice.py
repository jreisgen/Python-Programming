mylist = []
while True:
    item = int(input("New item: "))
    if item == 0:
        print("Bye!")
        break
    else:
        mylist.append(item)
        print(f"The list now: {mylist}")
        print(f"The list in order: {sorted(mylist)}")