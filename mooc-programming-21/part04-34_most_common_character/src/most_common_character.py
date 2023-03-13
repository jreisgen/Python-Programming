def most_common_character(message: str):
    newlist=[]
    for i in message:
        count = message.count(i)
        newlist.append(count)
    index = newlist.index(max(newlist))
    return message[index]
    
if __name__ == "__main__":
    second_string = "abc"
    print(most_common_character(second_string))
