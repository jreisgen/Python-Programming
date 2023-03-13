def line(int1, char):
    if char == "":
        print("*"*int1)
    else:
        print(char[0]*int1)
if __name__ == "__main__":
    line(5, "x")