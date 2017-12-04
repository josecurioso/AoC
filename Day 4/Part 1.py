import collections


invalid = 0
valid = 0
total = 0
lines = []



def isValid(line):
    line = line.split(" ")
    return len(set(line)) == len(line)




with open("input.txt", "r") as f:
    lines = f.readlines()




for i in lines:
    if isValid(i.strip()):
        valid += 1
    elif not isValid(i):
        invalid += 1
    total += 1

print("Invalid: " + str(invalid))
print("Valid: " + str(valid))


"""
if not isValid("qpq udci tnp fdfk kffd eyzvmg ufppf wfuodj toamfn tkze jzsb"):
    print("Invalid")
else:
    print("Valid")
"""
