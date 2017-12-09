import time

currentDepth = 0
score = 0
input = ""


with open("input.txt", "r") as f:
    input = list(''.join(f.readlines()))
"""

input = list("{<a>,<a>,<a>,<a>}")
"""
inGarbage = False
ignore = False
garbChars = 0

for i in input:
    if ignore:
        ignore = False
    elif not ignore:
        if (i == '!'):
            ignore = True
        elif (i == "{") and (not inGarbage):
            currentDepth += 1
            score += currentDepth
        elif (i== '<') and (not inGarbage) and (currentDepth>=1):
            inGarbage = True
        elif (i == '>') and inGarbage:
            inGarbage = False
        elif (i == '}') and (not inGarbage):
            currentDepth -= 1
        elif inGarbage:
            garbChars += 1
        if currentDepth<1:
            currentDepth = 1
    #time.sleep(0.0005)
print(score)
print(garbChars)
