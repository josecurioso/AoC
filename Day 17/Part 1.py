steps = 345
currentPos = 0
array = []
array.append(0)



for i in range(1, 2018):
    currentPos = (currentPos+steps)%len(array)
    array.insert(currentPos+1, i)
    currentPos += 1

print(array[currentPos+1])
