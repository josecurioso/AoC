import string
import time

pos = [0, 0]
lastChoice = ""
misc = list(string.ascii_lowercase)
misc = misc + list(string.ascii_uppercase)
lines = []
last = "d"
enc = []
steps = 0

with open("input.txt", "r") as f:
    for i in f.readlines():
        i = i[:-1]
        lines.append(list(i))

pos[1] = lines[0].index("|")

def goRight():
    global last
    global pos
    last = "r"
    pos[1] = pos[1] + 1

def goLeft():
    global last
    global pos
    last = "l"
    pos[1] = pos[1] - 1

def goUp():
    global last
    global pos
    last = "u"
    pos[0] = pos[0] - 1

def goDown():
    global last
    global pos
    last = "d"
    pos[0] = pos[0] + 1

def getSorround(pos):
    sorr = []
    try:
        if lines[pos[0]-1][pos[1]] != " ":
            sorr.append(lines[pos[0]-1][pos[1]])
        else:
            sorr.append("_")
    except:
        sorr.append("_")
    try:
        if lines[pos[0]][pos[1]+1] != " ":
            sorr.append(lines[pos[0]][pos[1]+1])
        else:
            sorr.append("_")
    except:
        sorr.append("_")
    try:
        if lines[pos[0]+1][pos[1]] != " ":
            sorr.append(lines[pos[0]+1][pos[1]])
        else:
            sorr.append("_")
    except:
        sorr.append("_")
    try:
        if lines[pos[0]][pos[1]-1] != " ":
            sorr.append(lines[pos[0]][pos[1]-1])
        else:
            sorr.append("_")
    except:
        sorr.append("_")
    return sorr

def isFinished(pos):
    sorr = getSorround(pos)

    if (last == "d"):
        sorr[0] = "_"
    elif (last == "u"):
        sorr[2] = "_"
    elif last == "r":
        sorr[3] = "_"
    elif last == "l":
        sorr[1] = "_"


    temp = ''.join(sorr)
    temp = temp.replace("_", "")

    if temp.strip() == "":
        return True
    else:
        return False

def getNewRoute(pos):
    global last
    sorr = getSorround(pos)

    if (last == "d"):
        sorr[0] = "_"
    elif (last == "u"):
        sorr[2] = "_"
    elif last == "r":
        sorr[3] = "_"
    elif last == "l":
        sorr[1] = "_"

    temp = ''.join(sorr)
    temp = temp.replace("_", "")
    indir = sorr.index(temp.strip())

    if indir == 0:
        goUp()
    elif indir == 1:
        goRight()
    elif indir == 2:
        goDown()
    elif indir == 3:
        goLeft()






done = False
while not done:
    steps += 1
    sorr = getSorround(pos)
    char = lines[pos[0]][pos[1]]
    #print(pos)
    #print(char)


    if isFinished(pos):
        done = True

    if char == "|":
        if (last == "d"):
            goDown()
        elif (last == "u"):
            goUp()
        elif last == "r":
            goRight()
        elif last == "l":
            goLeft()
    elif char == "-":
        if last == "d":
            goDown()
        elif last == "u":
            goUp()
        elif (last == "r"):
            goRight()
        elif (last == "l"):
            goLeft()
    elif char == "+":
        if (last == "d") and (sorr[2] != "-") and (sorr[2] != "_"):
            goDown()
        elif (last == "u") and (sorr[0] != "-") and (sorr[0] != "_"):
            goUp()
        elif (last == "r") and (sorr[1] != "|") and (sorr[1] != "_"):
            goRight()
        elif (last == "l") and (sorr[3] != "|") and (sorr[3] != "_"):
            goLeft()
        else:
            getNewRoute(pos)
    elif char in misc:
        enc.append(char)
        if last == "d":
            goDown()
        elif last == "u":
            goUp()
        elif last == "r":
            goRight()
        elif last == "l":
            goLeft()

print("Result: ", ''.join(enc))
print("Steps: ", steps)
