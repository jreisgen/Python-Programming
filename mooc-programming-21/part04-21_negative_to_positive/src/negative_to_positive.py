int1 = int(input("Please type in a positive integer: "))
negint = int1*-1
for i in range(negint, int1+1):
    if i != 0:
        print(i)