#Generator A starts with 783
#Generator B starts with 325

lastA = 783
lastB = 325

A_f = 16807
B_f = 48271

div = 2147483647

def generatePair():
    global lastA
    global lastB
    lastA = (A_f*lastA)%div
    lastB = (B_f*lastB)%div

def getBin(number):
    binary = str("{0:b}".format(number))
    return binary[-16:]



count = 0
for i in range(40000000):
    generatePair()
    if getBin(lastA) == getBin(lastB):
        count += 1

print(count)
