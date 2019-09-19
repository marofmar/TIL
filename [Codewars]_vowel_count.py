def getCount(inputStr):
    tmp = []
    v = ['a','e','i','o','u']
    sum = 0
    for ch in inputStr:
        tmp.append(ch)
    for j in tmp:
        if j in v:
            sum += 1
    return sum
