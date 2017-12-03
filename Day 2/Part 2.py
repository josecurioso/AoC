f = open("input.txt", "r")

matrix = []

for i in f.readlines():
    line = []
    for t in i.split("\t"):
        line.append(int(t))
    matrix.append(line)



resProv = []
for i in matrix:
    for t in i:
        for c in range(len(i)):
            if((t%i[c] == 0) and not(t == i[c])):
                resProv.append(t/i[c])


for i in range(len(matrix[0])):
    print([t for t in matrix[i]])


print()


result = 0
for i in resProv:
    result = result + i

print(result)
