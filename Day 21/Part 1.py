
data = dict()
keys = []

with open("input.txt", "r") as f:
    for i in f.readlines():
        i.replace("\n", "").strip()
        parts = i.split(" ")
        name = parts[0]
        result = parts[2]
        data[name] = result
        keys.append(name)

def multiply():
    global data
    length = len(keys)
    for i in keys:
        print(i)
        currentBatch = []
        result = data[i]

        last = list(i)
        for j in range(4):
            new = last
            if len(i) == 5:
                new[0] = last[3]
                new[1] = last[0]
                new[3] = last[4]
                new[4] = last[1]
            elif len(i) == 11:
                new[0] = last[8]
                new[1] = last[4]
                new[2] = last[0]
                new[4] = last[9]
                new[6] = last[1]
                new[8] = last[10]
                new[9] = last[6]
                new[10] = last[2]

            last = new
            currentBatch.append(''.join(new))

        flippedBatch = []
        for j in currentBatch:
            #Horiz flip
            newFlipped = j.split("/")
            newDone = []
            for e in newFlipped:
                separated = list(e)
                newDone = newDone + separated[::-1]
                newDone.append("/")
            newDone[len(newDone)-1] = ""

            newFlipped = ''.join(newDone)
            flippedBatch.append(newFlipped)

        count = 0
        currentBatch = currentBatch + flippedBatch
        for j in currentBatch:
            if j not in data:
                data[j] = result
                count += 1
        #print(count)

print(len(data))
multiply()
print(len(data))


def split(string):
    length = len(string.split("/")[0])
    newLen = length / 2
    for i in range(0, )

initial = ".#./..#/###"
new = data[initial]

new = split(new)

current = initial
new = ""
for i in range(5):
    current = data[current]
