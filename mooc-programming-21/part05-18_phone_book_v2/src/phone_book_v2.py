phoBook = {}
while True:
    inp = int(input("command(1 search, 2 add, 3 quit)"))
    if inp == 1:
        name = input("name: ")
        if name in phoBook:
            for i in phoBook[name]:
                print(i)
        else:
            print("no number") 
    elif inp == 2:
        name = input("name: ")
        number = (input("number: "))
        if name not in phoBook:
            phoBook[name] =list()
        phoBook[name].append(number)

        print("ok!")
    elif inp == 3:
        print("quitting...")
        break
    else:
        continue
