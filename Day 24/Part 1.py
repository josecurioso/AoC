pieces = []

with open("input.txt", "r") as f:
    pieces = [i.replace("\n", "").strip() for i in f.readlines()]


def getStarting():
    global pieces
    start = []
    for i in pieces:
        if i.split("/")[0] == "0":
            start.append(i)
    return start

def getNext(piece, num):
    global pieces
    pos = []

    for i in pieces:
        if num in i.split("/"):
            pos.append(i)

starting = getStarting()



def buildString(parts):




data = dict()
for i in starting:
    options = getNext(i, i.split("/")[1])
    for j in options:
        data[i][j] = get




    sides = i.split("/")

    posible = getPossible(i, sides[0])
