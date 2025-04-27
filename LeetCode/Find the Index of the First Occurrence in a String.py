def strStr(haystack, needle):
    res = -1
    num = len(needle)
    for i in range(num, len(haystack) + 1):
        if haystack[i - num:i] == needle:
            res = i - num
            break
    if haystack == needle:
        return 0
    return res


print(strStr("sadbutsad", "sad"))
print(strStr("leetcode", "leeto"))
print(strStr("a", "a"))
print(strStr("abc", "c"))
