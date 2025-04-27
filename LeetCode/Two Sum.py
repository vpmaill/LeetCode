def twoSum(nums, target):
    temp = []
    for i in nums:
        temp.append(i) if i < target else None
    res = []
    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            if temp[i] + temp[j] == target:
                res = [nums.index(temp[i]), nums.index(temp[j])]
    return res