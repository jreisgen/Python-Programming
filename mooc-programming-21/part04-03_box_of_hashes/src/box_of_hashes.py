def line(int1, char):
    if char == "":
        print("*"*int1)
    else:
        print(char[0]*int1)

def box_of_hashes(height):
    count = 0
    while count < height:
        line(10, "#")
        count +=1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
