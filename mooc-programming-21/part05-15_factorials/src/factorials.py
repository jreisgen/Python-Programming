def factorials(n: int):
    myDiction = {}
    newlist = []
    i = 2
    newlist.append(1)
    myDiction[1] = 1

    while i <= n:
        fact = 1
        j = i-0
        while j > 0:
            fact *= j
            j-=1
        newlist.append(fact)
        i+=1

        
    k = 1   
    h = 2 

    leng = len(newlist)
    while k < leng:
        myDiction[h] = newlist[k]
        k +=1
        h +=1
    
    return myDiction



if __name__ == "__main__":
    k = factorials(2)
    print(k[2])
    


