def lengthOfLongestSubstring(s):
    maxStringLength = 0
    tempString = ''
    for i in s:
        if i not in tempString:
            tempString += i
        else:
            maxStringLength = max(maxStringLength, len(tempString))
            tempString = tempString[tempString.find(i) + 1:]
            tempString += i
    return max(maxStringLength, len(tempString))


print(lengthOfLongestSubstring(" "))
