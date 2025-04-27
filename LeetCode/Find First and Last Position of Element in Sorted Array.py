def searchRange(nums, target):
    if target not in nums:
        return [-1, -1]
    left = 0
    right = len(nums) - 1
    res = [-1, -1]
    while left <= right:
        if nums[left] == target:
            res[0] = left
            break
        left += 1
    while right >= left:
        if nums[right] == target:
            res[1] = right
            break
        right -= 1
    return res


print(searchRange([1], 1))
