def all_the_longest(mylist):
    newlist = []
    finallist= []
    counter = 0
    for i in mylist:
        newlist.append(len(i))
    for i in newlist:
        if i == max(newlist):

            index = newlist.index(i, counter)

            finallist.append(mylist[index])
            counter = index+1
            
    return finallist


if __name__ == "__main__":
    print(all_the_longest(["heyho", "hei", "ofcourse", "eightlet"]))