original = []
originalCtrl = []

with open("input_test.txt", "r") as f:
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

    elif (a=="ne") and (b=="sw"):
        return "h"
    elif (a=="sw") and (b=="ne"):
        return "h"
    elif (a=="n") and (b=="s"):
        return "h"
    elif (a=="s") and (b=="n"):
        return "h"
    elif (a=="nw") and (b=="se"):
        return "h"
    elif (a=="se") and (b=="nw"):
        return "h"

    else:
        return "none"

def run():
    i = 0
    last = ""
    while i < len(original)-1:
        equivalent = getEquivalent(original[i], original[i+1])
        if equivalent == "none":
            i += 1
        elif equivalent == "h":
            original.pop(i+1)
            original.pop(i)

        else:
            original[i] = equivalent
            original.pop(i+1)


temp = 0
while temp != len(original):
    temp = len(original)
    run()


print(original)
print(len(original))
