items = int(input("How many items: "))
mylist=[]
counter = 1
while counter <= items:
    item1 = int(input(f"Item {counter}: "))
    mylist.append(item1)
    counter +=1
print(mylist)

