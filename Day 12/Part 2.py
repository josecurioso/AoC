import pprint
pp = pprint.PrettyPrinter(indent = 4)

ids = []
data = dict()
visited = []

with open("input.txt", "r") as f:
    for i in f.readlines():
        i.strip()
        i = i.split(" <-> ")
        id = int(i[0])
        ids.append(id)
        dest = [ int(e) for e in i[1].split(", ")]
        data[str(id)] = dest


#pp.pprint(data)


def getDests(id):
    visited.append(id)
    for i in data[str(id)]:
        if i not in visited:
            visited.append(i)
            getDests(i)

#getDests(0)

#print(len(visited))

count = 0
while len(ids) > 0:
    getDests(ids[0])
    for i in visited:
        ids.pop(ids.index(i))
        visited.remove(i)
    visited = []
    count += 1
print(count)
