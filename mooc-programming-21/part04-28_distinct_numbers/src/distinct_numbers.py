def distinct_numbers(mylist):
    newlist = []
    for i in mylist:
        if i not in newlist:
            newlist.append(i)
        
            
    return sorted(newlist)

if __name__=="__main__":
    distinct_numbers([1,2,1,4,5,2,4,3])