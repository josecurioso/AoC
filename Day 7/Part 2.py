import pprint

pp = pprint.PrettyPrinter(indent=4)
nodes = []
descendants = []
weights = dict()


tree = dict()

init = "hlhomy"

def getNodes():
    lines = []
    with open("input.txt", "r") as f:
        lines = f.readlines()
    return [i.split(" ")[0] for i in lines]

def getWeights():
    lines = []
    weights = dict()
    with open("input.txt", "r") as f:
        lines = f.readlines()
    for i in lines:
        name = i.split(" ")[0]
        number = i.split(" ")[1].strip()[1:len(i.split(" ")[1].strip())-1]
        weights[name] = int(number)
    return weights

def getDescend():
    lines = []
    desc = []
    with open("input.txt", "r") as f:
        lines = f.readlines()
    for i in lines:
        desc.append(i[(list(i).index(")")+5):].strip("\n").split(", "))
    return desc

weights = getWeights()
nodes = getNodes()
descendants = getDescend()



def GetTree(node):
    tree = dict()
    if descendants[nodes.index(node)] != "":
        for i in descendants[nodes.index(node)]:
            try:
                tree[i] = GetTree(i)
            except:
                pass
    return tree

def buildTree(node):
    tree = dict()
    tree[node] = GetTree(node)
    return tree


def calculateWeight(node):
    if node != "":
        sum = weights[node]
        if descendants[nodes.index(node)] != "":
            for i in descendants[nodes.index(node)]:
                sum += calculateWeight(i)
        return sum
    return 0


tree = buildTree(init)
#A bit tired when I got to this part I just did it manually
for i in descendants[nodes.index("rugzyaj")]:
    print(i, " ", calculateWeight(i))

print()
print(weights["apjxafk"])
