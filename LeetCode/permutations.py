def permute(nums):
    def delSame(lst):
        result = []
        for el in lst:
            if el not in result:
                result.append(el)
        return result

    if not nums:
        return []
    res = [[nums[0]]]
    for i in nums[1:]:
        tempArr = []
        for k in res:
            for j in range(len(k) + 1):
                tempEl = k[::]
                tempEl.insert(j, i)
                tempArr.append(tempEl)
                # tempArr[j + (len(k) - 1) * i].insert(j, nums[i])
            res = delSame(tempArr)[::]
    return res


print(sorted(permute([1, 2, 3])))
