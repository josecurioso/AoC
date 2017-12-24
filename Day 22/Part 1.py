

def getLines(filename):
    grid = []
    lines = []
    with open(filename, "r") as f:
        lines = [i.replace("\n", "").strip() for i in f.readlines()]

        for i in lines:
            grid.append(list(i))
    return grid

grid = getLines("input.txt")
coord = [len(grid)/2, len(grid[0])/2]

print(coord)


"""
for i in range(10000):
    task
"""
