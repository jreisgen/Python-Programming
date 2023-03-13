def remove_smallest(numbers: list):
    newone = numbers[:]
    newone.sort()
    smallest = newone[0]
    index = numbers.index(smallest)
    del numbers[index]
    




if __name__ == "__main__":
    numbers = [2,1,3,4,2]
    remove_smallest(numbers)
    print(numbers)