things = "abcdefghijklmnop"
things = list(things)

instructions = []

with open("input.txt", "r") as f:
    text = ''.join(f.readlines()).strip()
    instructions = text.split(',')



def spin(l, n):
    return l[-n:] + l[:-n]

def exchange(l, pos):
    l[int(pos[1])],l[int(pos[0])] = l[int(pos[0])], l[int(pos[1])]
    return l

def partner(l, names):
    A, B = l.index(names[0]),l.index(names[1])
    l[A], l[B] = l[B], l[A]
    return l

print(things)

for i in instructions:
    if i[0] == 's':
        i = i[1:]
        things = spin(things, int(i))
    if i[0] == 'x':
        i = i[1:]
        split = i.split('/')
        things = exchange(things, split)

    if i[0] == 'p':
        i = i[1:]
        split = i.split('/')
        things = partner(things, split)

print(''.join(things))
