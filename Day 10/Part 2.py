from functools import reduce

values = [i for i in range(256)]
lengths = []
dense = []
currentIndex = 0
skipSize = 0


def getInput(filename):
    lengths = []
    with open(filename, "r") as f:
        lengths = [int(ord(i)) for i in list(f.readline().replace("\n", ""))]
        lengths.append(17)
        lengths.append(31)
        lengths.append(73)
        lengths.append(47)
        lengths.append(23)
    return lengths


def flip(currentIndex, length):
    saved = []
    while (length)>0:
        intend = currentIndex+length-1
        while intend >= len(values):
            intend -= len(values)
        saved.append(values[intend])
        length -= 1
    for i in saved:
        while currentIndex >= len(values):
            currentIndex -= len(values)
        values[currentIndex] = i
        currentIndex += 1


def getDense(values):
    dense = []
    for i in range(0, 256, 16):
        sh = reduce(lambda x, y: x ^ y, values[i:i+16])
        dense.append(sh)
    return dense


def convertHex(dense):
    return ''.join(["%0.2x" % i for i in dense])

def runRound():
    global currentIndex
    global skipSize
    for i in lengths:
        if currentIndex >= len(values):
            currentIndex -= len(values)
        flip(currentIndex, i)
        currentIndex += i
        currentIndex += skipSize
        skipSize += 1




lengths = getInput("input.txt")
print(lengths)
for a in range(64):
    print("a")
    runRound()
dense = getDense(values)
print(dense)
finalHash = convertHex(dense)

print(finalHash)
"""

test = [64, 7, 255]


print(convertHex(test))


33efeb34ea91902bb2f59c9920caa6cd
"""
