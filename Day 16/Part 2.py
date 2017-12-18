things = "abcdefghijklmnop"
original = things
things = list(things)
instructions = []

with open("input.txt", "r") as f:
    text = ''.join(f.readlines()).strip()
    instructions = text.split(',')


def partner(l, names):
    A, B = l.index(names[0]),l.index(names[1])
    l[A], l[B] = l[B], l[A]
    return l

print(things)

for i in range(64):
    if ''.join(things) == original:
        print(i)
    for i in instructions:
        if i[0] == 's':
            things = things[-int(i[1:]):] + things[:-int(i[1:])]
        if i[0] == 'x':
            pos = i[1:].split('/')
            things[int(pos[1])], things[int(pos[0])] = things[int(pos[0])], things[int(pos[1])]
        if i[0] == 'p':
            split = i[1:].split('/')
            A, B = things.index(split[0]),things.index(split[1])
            things[A], things[B] = things[B], things[A]

print(''.join(things))
