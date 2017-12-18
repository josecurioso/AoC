import string
import time

instructions = []
data = dict()
lastFreq = 0
pos = -1
abc = list(string.ascii_lowercase)
done = False

with open("input.txt", "r") as f:
    instructions = f.readlines()

for i in abc:
    data[i] = 0

def snd(param):
    global lastFreq
    print("Playing freq: ", data[param])
    lastFreq = data[param]

def set(param, param2):
    if param2 in abc:
        num = data[param2]
        data[param] = num
    else:
        data[param] = int(param2)

def mul(param, param2):
    num = 0
    if param2 in abc:
        num = data[param2]
    else:
        num = int(param2)
    data[param] = data[param] * num

def jgz(param, num):
    global pos
    val = 0
    if param in abc:
        val = data[param]
    else:
        val = int(param)
    if val > 0:
        print("Jump: ", int(num))
        pos += int(num)-1
        print("After jump: ", pos)

def mod(param, param2):
    if param2.strip() in abc:
        data[param] = data[param] % data[param2]
    else:
        val = int(param2)
        data[param] = data[param] % val

def add(param, param2):
    if param2 in abc:
        data[param] = data[param] + data[param2]
    else:
        data[param] = data[param] + int(param2)

def rcv(param):
    global done
    val = data[param]
    if val != 0:
        print("The last freq played was: ", lastFreq)
        done = True

while not done:
    pos += 1
    instructions[pos] = instructions[pos].replace("\n", "")
    split = instructions[pos].split(' ')

    #print(pos)
    #time.sleep(0.5)
    if split[0] == 'snd':
        snd(split[1])

    if split[0] == 'set':
        set(split[1], split[2])

    if split[0] == 'mul':
        mul(split[1], split[2])

    if split[0] == 'jgz':
        jgz(split[1], split[2])

    if split[0] == 'mod':
        mod(split[1], split[2])

    if split[0] == 'add':
        add(split[1], split[2])

    if split[0] == 'rcv':
        rcv(split[1])
"""

data['a'] = 1

data['b'] = 2

pos = 10

jgz('a', -5)

print(pos)
"""
