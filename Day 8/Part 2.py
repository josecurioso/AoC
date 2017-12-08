vars = dict()
seen = []

interNumbers = []

def parseLine(line):
    sepL = line.split(" ")
    var = sepL[0]
    op = sepL[1]
    num = sepL[2]
    condVar = sepL[4]
    cond = sepL[5]
    condNum = sepL[6]
    return var, op, int(num), condVar, cond, int(condNum)

def evaluate(line):
    var, op, num, condVar, cond, condNum = parseLine(line)

    boolean = 0

    if condVar not in seen:
        seen.append(condVar)
        vars[condVar] = 0

    if cond == "==":
        boolean = (vars[condVar] == condNum)
    if cond == "!=":
        boolean = (vars[condVar] != condNum)
    if cond == "<=":
        boolean = (vars[condVar] <= condNum)
    if cond == ">=":
        boolean = (vars[condVar] >= condNum)
    if cond == "<":
        boolean = (vars[condVar] < condNum)
    if cond == ">":
        boolean = (vars[condVar] > condNum)

    if var not in seen:
        seen.append(var)
        vars[var] = 0

    if boolean:
        if op == "dec":
            vars[var] -= num
        elif op == "inc":
            vars[var] += num
        interNumbers.append(vars[var])



with open("input.txt", "r") as f:
    for i in f.readlines():
        evaluate(i)
    print(max(interNumbers))
