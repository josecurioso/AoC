insertPos = 0
value = 0


for i in range(1, 50000001):
    insertPos = ((insertPos+345)%i)+1
    if insertPos == 1:
        value = i

print(value)
