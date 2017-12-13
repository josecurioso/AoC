places = []
directions = []
currentSpot = -1

with open("input.txt", "r") as f:
    for i in f.readlines():
        i = i.strip()
        data = i.split(": ")
        places[int(data[0])] = ["" for e in range(int(data[1]))]


def placePatrols():
	for i in places:
  	    i[0] = "S"
  	    directions.append(true)

def updatePatrols():
    counter = 0
    for i in places:
  	     cell = i.index("S")
         if directions[counter] and (cell+1)<=(len(i)-1):
             i[cell] = ""
    	     i[cell+1] = "S"
         elif directions[counter] and (cell+1)>(len(i)-1):
             directions[counter] = not directions[counter]
             i[cell] = ""
             i[cell-1] = "S"
         elif (not directions[counter]) and (cell-1)>=0:
             i[cell] = ""
             i[cell-1] = "S"
         elif (not directions[counter]) and (cell-1)<0):
             directions[counter] = not directions[counter]
             i[cell] = ""
             i[cell+1] = "S"
         counter += 1
