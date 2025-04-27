def fourSum(nums, target):
    nums.sort()
    s = set()
    output = []
    for i in range(len(nums)):
        for t in range(i + 1, len(nums)):
            j = t + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[t] + nums[j] + nums[k]
                if sum == target:
                    s.add((nums[i], nums[t], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum < target:
                    j += 1
                else:
                    k -= 1
    output = list(s)
    return output


print(fourSum([1, 0, -1, 0, -2, 2], 0))