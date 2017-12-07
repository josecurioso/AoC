input = "5 1 10 0 1 7 13 14 3 12 8 10 7 12 0 6"

input = [int(i) for i in input.split(" ")]

unique = []

actual = input
totalAmount = len(input)

cycles = 0

while ' '.join(str(e) for e in actual) not in unique:
    unique.append(' '.join(str(e) for e in actual))
    redist = max(actual)
    maxIndex = actual.index(redist)

    actual[maxIndex] = 0
    ind = maxIndex
    while redist > 0:
        ind += 1
        if ind>=totalAmount:
            ind = 0

        actual[ind] += 1
        redist -= 1
    cycles += 1

    #print(actual)

print("Part1: ", cycles)
print("Part2: ", cycles-unique.index(' '.join(str(e) for e in actual)))
