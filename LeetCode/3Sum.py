def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    target = 0
    nums.sort()
    s = set()
    output = []
    for i in range(len(nums)):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum == target:
                s.add((nums[i], nums[j], nums[k]))
                j += 1
                k -= 1
            elif sum < target:
                j += 1
            else:
                k -= 1
    output = list(s)
    return output


print(threeSum([1, 0, -1, 0, -2, 2]))
