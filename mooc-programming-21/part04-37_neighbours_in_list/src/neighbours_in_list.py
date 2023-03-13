def longest_series_of_neighbours(mylist: list):
    newlist = []
    counter = 1
    i = 0
    while i <= len(mylist)-2:
        if abs(mylist[i] - mylist[i+1]) <= 1:
            counter += 1
        else:
            newlist.append(counter)
            counter = 1
        i+=1
        newlist.append(counter)
             
    return max(newlist)
if __name__ == "__main__":
    hi = longest_series_of_neighbours([1,2])
    print(hi)