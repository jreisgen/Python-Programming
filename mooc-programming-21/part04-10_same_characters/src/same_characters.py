def same_chars(char, int1, int2):
    if len(char)-1 < int2 or len(char)-1 < int1:
        return False
    elif char[int1] == char[int2]:
        return True
    else:
        return False 
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))