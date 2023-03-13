def line(int1, char):
    if char == "":
        print("*"*int1)
    else:
        print(char[0]*int1)


def triangle(size, char):
    counter = 0
    while counter <= size:
        line(counter, char)
        counter +=1

def rectangle(width, height, char):
    counter = 0
    while counter < height:
        print(width*char)
        counter+=1

def shape(width, char1, height, char2):
    triangle(width, char1)
    rectangle(width, height, char2)

        # You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")