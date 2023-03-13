def who_won(gameboard: list):
    ones = 0
    twos = 0
    for row in gameboard:
        for element in row:
            if element == 1:
                ones +=1
            elif element == 2:
                twos += 1
            else:
                continue
    if ones > twos:
        return 1
    elif twos > ones:
        return 2
    else:
        return 0