def list_of_stars(mylist):
    for i in range(0, len(mylist)):
        print("*"*mylist[i])

if __name__ == "__main__":
    list_of_stars([1,5,3,5,2,5])
