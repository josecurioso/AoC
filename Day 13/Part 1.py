places = dict()
directions = dict()
currentSpot = -1
caught = 0
ids = []

with open("input.txt", "r") as f:
    for i in f.readlines():
        i = i.strip()
        data = i.split(": ")
        ids.append(int(data[0]))
        places[str(data[0])] = ["" for e in range(int(data[1]))]


def placePatrols():
    for i in ids:
        places[str(i)][0] = "S"
        directions[str(i)] = True

def updatePatrols():
    for i in ids:
        cell = places[str(i)].index("S")
        if directions[str(i)] and (cell+1)<=(len(places[str(i)])-1):
            places[str(i)][cell] = ""
            places[str(i)][cell+1] = "S"
        elif directions[str(i)] and (cell+1)>(len(places[str(i)])-1):
            directions[str(i)] = not directions[str(i)]
            places[str(i)][cell] = ""
            places[str(i)][cell-1] = "S"
        elif (not directions[str(i)]) and (cell-1)>=0:
            places[str(i)][cell] = ""
            places[str(i)][cell-1] = "S"
        elif (not directions[str(i)]) and (cell-1)<0:
            directions[str(i)] = not directions[str(i)]
            places[str(i)][cell] = ""
            places[str(i)][cell+1] = "S"

def addCaught(place, currentSpot):
    return currentSpot * len(place)

placePatrols()
while currentSpot < 98:
    currentSpot+=1
    if currentSpot in ids:
        if(places[str(currentSpot)][0] == "S"):
            caught += addCaught(places[str(currentSpot)], currentSpot)
    updatePatrols()

print(caught)
