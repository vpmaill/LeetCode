def myAtoi(s):
    s = s.strip()
    tempString = ''
    isNeg = False
    try:
        if s[0] == '-':
            s = s[1::]
            isNeg = True
        elif s[0] == "+":
            s = s[1::]
    except Exception:
        None
    i = 0
    while i < len(s):
        if s[0] == '0':
            s = s[1::]
        else:
            break
        i += 1
    i = 0
    while i < len(s):
        if s[i] in "1234567890":
            tempString += s[i]
        else:
            break
        i += 1
    if tempString == '':
        return 0
    elif int(tempString) > 2**31 and isNeg:
        return -2**31
    elif int(tempString) > 2**31 - 1 and not isNeg:
        return 2**31 - 1
    else:
        if isNeg:
            tempString = "-" + tempString
        return int(tempString)


print(myAtoi(""))
print(myAtoi("010"))
print(myAtoi(" -042"))
print(myAtoi("-91283472332"))