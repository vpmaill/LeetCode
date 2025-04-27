def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    while (right - left) > 1:
        temp = (right + left) // 2
        if nums[temp] == target:
            return temp
        elif nums[temp] > target:
            right = temp
        else:
            left = temp
    if nums[left] == target:
        return left
    elif target > nums[right]:
        return right + 1
    elif target < nums[left]:
        return left
    else:
        return left + 1


print(searchInsert([1, 3, 5, 6], 5))
print(searchInsert([1, 3, 5, 6], 2))
print(searchInsert([1, 3, 5, 6], 7))
print(searchInsert([1, 3, 5, 6], 0))
print(searchInsert([1], 1))
