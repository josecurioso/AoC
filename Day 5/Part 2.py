def getInput():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        return [int(i) for i in lines]

counter = 0
currentIndex = 0
lines = getInput()
tempMove = 0

while (0<=currentIndex<=1090):
    try:
        tempMove = lines[currentIndex]
        if abs(tempMove)>=3:
            if tempMove<0:
                lines[currentIndex] = lines[currentIndex]+1
            else:
                lines[currentIndex] = lines[currentIndex]-1
        else:
            lines[currentIndex] = lines[currentIndex]+1
        currentIndex += tempMove
        #print("Current: lines[", currentIndex+1, "] = ", lines[currentIndex], " | isOut ", not(0<=currentIndex<=1090))
        counter += 1
    except:
        break


print(counter)
