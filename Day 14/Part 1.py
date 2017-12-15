import numpy as np


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

    bstr = ''.join(sequence)
    integer = int(bstr, 16)
    hstr = format(integer, '0>42b')
    return hstr


sequence = list(str(getSequence("nbysizxe")))
print(sequence.count("1"))
