original = []
new = []
originalNew = []

with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [i.strip() for i in lines]
    lines = ''.join(lines)
    original = lines.split(",")


def getEquivalent(a, b):
    if (a=="se") and (b=="sw"):
        return "s"
    elif (a=="sw") and (b=="se"):
        return "s"

    elif (a=="nw") and (b=="s"):
        return "sw"
    elif (a=="s") and (b=="nw"):
        return "sw"

    elif (a=="sw") and (b=="n"):
        return "nw"
    elif (a=="n") and (b=="sw"):
        return "nw"

    elif (a=="nw") and (b=="ne"):
        return "n"
    elif (a=="ne") and (b=="nw"):
        return "n"

    elif (a=="n") and (b=="se"):
        return "ne"
    elif (a=="se") and (b=="n"):
        return "ne"

    elif (a=="ne") and (b=="s"):
        return "se"
    elif (a=="s") and (b=="ne"):
        return "se"
    else:
        return "none"






for j in range(500):
    i = 0
    while i < len(original)-1:
        equivalent = getEquivalent(original[i], original[i+1])
        if equivalent == "none":
            i += 1
        else:
            original[i] = equivalent
            print(original.pop(i+1))

print(original)
