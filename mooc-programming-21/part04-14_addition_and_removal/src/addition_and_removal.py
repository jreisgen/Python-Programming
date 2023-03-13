mylist = []
counter = 1
while True:
    print(f"The list is now {mylist}")
    letter = input("a(d)d. (r)emove or e(x)it: ")
    if letter == "d":
        mylist.append(counter)
        counter +=1
        
    elif letter == "r":
        last = len(mylist)-1
        mylist.pop(last)
        
        counter -=1
    else:
        print("Bye!")
        break

