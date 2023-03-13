import copy
def invert(dictionary: dict):
    i = 0
    
    invDictionary = copy.deepcopy(dictionary)
    dictionary.clear()
    leng = len(invDictionary)
    while i < leng:
        key = list(invDictionary)[0]
        value = invDictionary[key]
        del invDictionary[key]
        dictionary[value] = key
        i+=1


    

if __name__ == "__main__":
    myDictionary = {"name": "myName", "age": "myAge"}
    invert(myDictionary)
    print(myDictionary)
