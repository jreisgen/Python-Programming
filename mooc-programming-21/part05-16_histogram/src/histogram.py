def histogram(str):
    stars = {}
    leng = len(str)
    i = 0
    while i < leng:
        letter = str[i]
        if letter in stars:
            stars[letter] +=1
        else:
            stars[letter] = 1
        i+=1
    
    for key, value in stars.items():

       print(key, value * "*")

    

    

if __name__ == "__main__":

    histogram("heyho")
   
    


