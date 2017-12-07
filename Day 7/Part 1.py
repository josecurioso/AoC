
nodes = []
descend = []


def getNodes():
    lines = []
    with open("input.txt", "r") as f:
        lines = f.readlines()
    return [i.split(" ")[0] for i in lines]

def getDescend():
    lines = []
    desc = []
    with open("input.txt", "r") as f:
        lines = f.readlines()
    for i in lines:
        temp = i[(list(i).index(")")+5):].strip("\n")
        if temp != "":
            desc += temp.split(", ")

    return desc
    #return [.split(", ") for i in lines]

nodes = getNodes()
descend = getDescend()
for i in nodes:
    if i not in descend:
        print(i)
