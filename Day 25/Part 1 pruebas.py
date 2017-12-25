state = 'A'
steps = 12302209
cursor = 0
ones = set()

def iterate():
    global state
    global cursor
    global ones
    if state == 'A':
        if cursor in ones:
            ones.remove(cursor)
            cursor -= 1
            state = 'D'
        else:
            ones.add(cursor)
            cursor += 1
            state = 'B'
    elif state == 'B':
        if cursor in ones:
            ones.remove(cursor)
            cursor += 1
            state = 'F'
        else:
            ones.add(cursor)
            cursor += 1
            state = 'C'
    elif state == 'C':
        if cursor in ones:
            ones.add(cursor)
            cursor -= 1
            state = 'A'
        else:
            ones.add(cursor)
            cursor -= 1
            state = 'C'
    elif state == 'D':
        if cursor in ones:
            ones.add(cursor)
            cursor += 1
            state = 'A'
        else:
            cursor -= 1
            state = 'E'
    elif state == 'E':
        if cursor in ones:
            ones.remove(cursor)
            cursor += 1
            state = 'B'
        else:
            ones.add(cursor)
            cursor -= 1
            state = 'A'
    elif state == 'F':
        if cursor in ones:
            ones.remove(cursor)
            cursor += 1
            state = 'E'
        else:
            cursor += 1
            state = 'C'

for i in range(steps):
    iterate()
print(len(ones))
