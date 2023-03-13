def first_word(message: str):
    counter = 0
    while message[counter] != " " and counter < len(message)-1:
        counter +=1
    return message[0: counter]

def second_word(message: str):    
    first = len(first_word(message))
    second = message[first+1:]
    if len(message) == len(first_word(message)) + len(first_word(second)) + 2:
        return first_word(second) + message[-1]

    return first_word(second)


def last_word(message: str):
    int1 = -1
    while message[int1] != " ":
        int1 -=1
    return message[int1+1: -1]  + message[-1]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))