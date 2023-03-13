# Write your solution here

def palindromes(message: str):
    leng = len(message)
    str = ""
    for i in range(leng-1, -1, -1):
        str += message[i]
    if str == message:
        return True

    else:
        return False

while True:
    input1 = input("Please type in a palindrome: ")
    if palindromes(input1):
        print(f"{input1} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
    










# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
