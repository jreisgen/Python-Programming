def times_ten(start_index: int, end_index: int):
    dictionary = {}
    i = 0
    j = 1
    diff = end_index-start_index
    while i <= diff:
        dictionary[start_index+i] = (start_index+i)* (10)
        i+=1
        j+=1
    return dictionary
