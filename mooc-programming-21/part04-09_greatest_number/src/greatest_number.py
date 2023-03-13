def greatest_number(int1, int2, int3):
    biggest = 0
    if int2 > int3:
        biggest = int2
    else:
        biggest = int3
    if int1 > biggest:
        biggest = int1
        return biggest
    else:
        return biggest

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)