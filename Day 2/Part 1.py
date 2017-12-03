f = open("input.txt", "r")

matrix = []


for i in f.readlines():
    line = []
    for t in i.split("\t"):
        line.append(int(t))
    matrix.append(line)



mins = []
for i in matrix:
    minLinea = i[0]
    for t in i:
        if(t < minLinea):
            minLinea = t
    mins.append(minLinea)


maxs = []
for i in matrix:
    maxLinea = 0
    for t in i:
        if(t > maxLinea):
            maxLinea = t
    maxs.append(maxLinea)


for i in range(len(matrix[0])):
    print([t for t in matrix[i]])


print()


result = 0
for i in range(len(matrix)):
    inter = (maxs[i] - mins[i])
    result = result + inter
    print(str(maxs[i]) + " - " +  str(mins[i]) + " = " + str(inter) + "    res: " + str(result))
