#values = [i for i in range(20)]
values = [i for i in range(256)]
lengths = []
currentIndex = 0
skipSize = 0


with open("input.txt", "r") as f:
    lengths = [int(i.replace("\n", "")) for i in f.readline().split(",")]

def flip(currentIndex, length):
    saved = []
    while (length)>0:
        intend = currentIndex+length-1
        if intend >= len(values):
            intend -= len(values)
        saved.append(values[intend])
        length -= 1
    for i in saved:
        if currentIndex >= len(values):
            currentIndex -= len(values)
        values[currentIndex] = i
        currentIndex += 1


for i in lengths:
    if currentIndex >= len(values):
        currentIndex -= len(values)
    flip(currentIndex, i)
    currentIndex += i
    currentIndex += skipSize
    skipSize += 1


print(values[0]*values[1])
