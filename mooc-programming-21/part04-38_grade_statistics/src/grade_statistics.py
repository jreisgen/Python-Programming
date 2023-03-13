failed = 0
supertotalpoints = 0
people = 0
zeros = 0
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0


while True:
    doubleint = input("Exam points and exercises completed: ")
    if doubleint == "":
        passper = 100-((failed/people)*100)
        average = supertotalpoints/people
        print("Statistics: ")
        print("Points average: " + "{:.1f}".format(average))
        print("Pass percentage: " + "{:.1f}".format(passper))
        print("Grade distribution: ")
        print("5: " + ("*"*fives))
        print("4: " + ("*"*fours))
        print("3: " + ("*"*threes))
        print("2: " + ("*"*twos))
        print("1: " + ("*"*ones))
        print("0: " + ("*"*zeros))
        break


    else: 
        blankdex = doubleint.index(" ")
        firstgrade = int(doubleint[0: blankdex])
        secondgrade = int(doubleint[blankdex+1: ])
        secondpoints = secondgrade // 10
        totalpoints = firstgrade + secondpoints
        supertotalpoints += totalpoints
        people +=1
        if firstgrade < 10:
            failed+=1
            zeros +=1
            totalpoints = 0
        if totalpoints >= 28:
            fives +=1
        elif totalpoints >=24:
            fours +=1
        elif totalpoints >=21:
            threes +=1
        elif totalpoints >= 18:
            twos +=1
        elif totalpoints >= 15:
            ones +=1
        else:
            if firstgrade >= 10:
                zeros +=1
                failed +=1
    


    
