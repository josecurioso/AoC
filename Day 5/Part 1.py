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
        lines[currentIndex] = lines[currentIndex]+1
        currentIndex += tempMove
        #print("Current: lines[", currentIndex+1, "] = ", lines[currentIndex], " | isOut ", not(0<=currentIndex<=1090))
        counter += 1
    except:
        break


print(counter)
