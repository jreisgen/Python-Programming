# Copy here code of line function from previous exercise
def line(int1, char):
    if char == "":
        print("*"*int1)
    else:
        print(char[0]*int1)

def triangle(size):
    counter = 0
    while counter <= size:
        line(counter, "#")
        counter +=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
