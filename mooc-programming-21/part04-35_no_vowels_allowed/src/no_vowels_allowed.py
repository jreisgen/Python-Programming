def no_vowels(message: str):
    newstring = ""
    for i in message:
        if i != "a" and i !="e" and i !="o" and i !="i" and i !="u":
            newstring +=i
    return newstring
            
    


if __name__=="__main__":
    hi = no_vowels("heyhohey")
    print(hi)