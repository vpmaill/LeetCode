def countAndSay(n: int) -> str:
    tempString = '1'
    res = '1'
    for j in range(n - 1):
        res = ''
        tempValue = 1
        for i in range(1, len(tempString)):
            if tempString[i] == tempString[i - 1]:
                tempValue += 1
            else:
                res += str(tempValue) + tempString[i - 1]
                tempValue = 1
        res += str(tempValue) + tempString[-1]
        tempString = res
    return res


print(countAndSay(1))
print(countAndSay(2))
print(countAndSay(3))
print(countAndSay(4))