def dict_of_numbers():
    numbers = {}
    
    i = 0
    while i < 100:
        numbers[i] = i
        i+=1

    numbers[0] = "zero"
    numbers[1] = "one"
    numbers[2] = "two"
    numbers[3] = "three"
    numbers[4] = "four"
    numbers[5] = "five"
    numbers[6] = "six"
    numbers[7] = "seven"
    numbers[8] = "eight"
    numbers[9] = "nine"
    numbers[10] = "ten"
    numbers[11] = "eleven"
    numbers[12] = "twelve"
    numbers[13] = "thirteen"
    numbers[14] = "fourteen"
    numbers[15] = "fifteen"
    numbers[16] = "sixteen"
    numbers[17] = "seventeen"
    numbers[18] = "eighteen"
    numbers[19] = "nineteen"
    numbers[20] = "twenty"
    numbers[30] = "thirty"
    numbers[40] = "forty"
    numbers[50] = "fifty"
    numbers[60] = "sixty"
    numbers[70] = "seventy"
    numbers[80] = "eighty"
    numbers[90] = "ninety"
    
    
    for key in numbers:
        if key > 20 and key%10 != 0:
            modu = key % 10
            tens = (key // 10)*10
            numbers[key] = numbers[tens] + "-" + numbers[modu]
        

    return numbers