def range_of_list(mylist):
    sorted1 = sorted(mylist)
    range = sorted1[-1]-sorted1[0]
    return range

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)