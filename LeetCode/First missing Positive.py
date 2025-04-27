def firstMissingPositive(nums):
    res = 1
    while res in nums:
        res += 1
    return res