def spruce(int1):
    print("a spruce!")
    counter = 1
    stars = 1
    total = int(int1*2-1)
    blank = int(total/2)
    while counter <= int1:
        print(" "*blank + "*"*stars+ " "*blank)
        blank -=1
        counter +=1
        stars +=2
    blank = int(total/2)
    print(" "*blank + "*"+ ""*blank)
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)