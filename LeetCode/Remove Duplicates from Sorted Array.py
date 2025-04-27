def removeDuplicates(nums):
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j, nums


nums = [0, 0, 1, 1, 2, 3]
expectedNums = [0, 1, 2, 3]
k, res = removeDuplicates(nums)

print(res)
