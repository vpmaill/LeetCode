def groupAnagrams(strs):
    res = {}
    for i in strs:
        temp = "".join(sorted(i))
        if temp not in res:
            res[temp] = [i]
            continue
        res[temp].append(i)
    return list(res.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
