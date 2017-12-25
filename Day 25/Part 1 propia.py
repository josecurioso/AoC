state = "A"
pos = 0
tape = dict()






for i in range(12302209):
    reading = ""
    if str(pos) in tape.keys():
        reading = tape[str(pos)]
    else:
        reading = "0"

    if (state=="A") and (reading=="0"):
        state = "B"
        tape[str(pos)] = "1"
        pos += 1
    if (state=="A") and (reading=="1"):
        state = "D"
        tape[str(pos)] = "0"
        pos -= 1

    if (state=="B") and (reading=="0"):
        state = "C"
        tape[str(pos)] = "1"
        pos += 1
    if (state=="B") and (reading=="1"):
        state = "F"
        tape[str(pos)] = "0"
        pos += 1

    if (state=="C") and (reading=="0"):
        state = "C"
        tape[str(pos)] = "1"
        pos -= 1
    if (state=="C") and (reading=="1"):
        state = "A"
        tape[str(pos)] = "1"
        pos -= 1

    if (state=="D") and (reading=="0"):
        state = "E"
        tape[str(pos)] = "0"
        pos -= 1
    if (state=="D") and (reading=="1"):
        state = "A"
        tape[str(pos)] = "1"
        pos += 1

    if (state=="E") and (reading=="0"):
        state = "A"
        tape[str(pos)] = "1"
        pos -= 1
    if (state=="E") and (reading=="1"):
        state = "B"
        tape[str(pos)] = "0"
        pos += 1

    if (state=="F") and (reading=="0"):
        state = "C"
        tape[str(pos)] = "0"
        pos += 1
    if (state=="F") and (reading=="1"):
        state = "E"
        tape[str(pos)] = "0"
        pos += 1
    print(state)
    print(pos)
    print(reading)

print(tape)
