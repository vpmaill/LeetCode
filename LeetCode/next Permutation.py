def nextPermutation(nums):
    arr = [[nums[0]]]
    for i in nums[1::]:
        tempList = []
        for j in arr:
            for k in range(len(j) + 1):
                tempel = j[::]
                tempel.insert(k, i)
                if tempel not in tempList:
                    tempList.append(tempel)
        arr = tempList
    arr.sort()
    nums[:] = arr[(arr.index(nums) + 1) % len(arr)]
    return nums


print(nextPermutation([1, 1, 5]))
