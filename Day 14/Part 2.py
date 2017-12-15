import numpy as np
import time
import binascii

def knotHash(lengths):
    """Part 2."""

    skip = 0
    position = 0
    inputs = list(range(256))
    lengths = [ord(i) for i in lengths] + [17, 31, 73, 47, 23]

    n = 256
    skip = 0
    position = 0
    for rounds in range(64):
        for length in lengths:
            step = position + length
            if step > n:
                idx =  position
                inputs = np.roll(inputs, -idx)
                inputs[:length] = list(reversed(inputs[:length]))
                inputs = np.roll(inputs, idx)
            else:
                inputs[position: step] = list(reversed(inputs[position: step]))

            position = (position + length + skip) % n
            skip += 1

    dense = []
    for i in range(16):
        group = inputs[16*i : 16*i + 16]
        val = np.bitwise_xor.reduce(group)
        dense.append("{:02x}".format(val))
    dense = ''.join(dense).strip()
    return dense

def getSequence(string):
    sequence = []
    for i in range(128):
        sequence.append(knotHash(string + "-" + str(i)))


    for i in range(len(sequence)):
        integer = int(sequence[i], 16)
        sequence[i] = list(format(integer, '0>128b'))

    """
    integer = int(''.join(sequence), 16)
    sequence = format(integer, '0>42b')
    """

    return sequence


#nbysizxe
sq = getSequence("nbysizxe")
#print(sq)

def markArea(line, index, number):
    global sq
    #print("Number of rows: ", len(sq))
    #print("Number of columns: ", len(sq[line]))
    #time.sleep(0.005)
    #print(len(sq[line]))
    if sq[line][index] == "1":
        sq[line][index] = str(number)
        ind = index - 1
        if (ind>=0) and (ind<len(sq[line])):
            markArea(line, ind, number)
        ind = index + 1
        if (ind>=0) and (ind<len(sq[line])):
            markArea(line, ind, number)
        lin = line - 1
        if (lin>=0) and (lin<len(sq)):
            markArea(lin, index, number)
        lin = line + 1
        if (lin>=0) and (lin<len(sq)):
            markArea(lin, index, number)
        return True
    return False



current = 2
for i in range(len(sq)):
    for j in range(len(sq[i])):
        if markArea(i, j, current):
            current += 1

print("Number of groups: ", current-2)
