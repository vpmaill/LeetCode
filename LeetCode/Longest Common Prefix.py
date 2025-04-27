def longestCommonPrefix(strs):
    res = ""
    for i in range(min(map(lambda x: len(x), strs))):
        tempSymb = strs[0][i]
        flag = True
        for j in strs:
            if j[i] != tempSymb:
                flag = False
        if flag:
            res += tempSymb
    return res