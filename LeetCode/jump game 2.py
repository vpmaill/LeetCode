def jump(nums):
    def searchMax(arr: list[int]):
        m = 0
        res = 0
        for i in range(len(arr)):
            if m < (arr[i] + i):
                m = arr[i] + i
                res = i
        return res

    if len(nums) == 1:
        return 1
    jumps = 0
    i = 0
    j = nums[0]
    while i + j < len(nums) - 1:
        i = i + searchMax(nums[i:i+j+1])
        j = nums[i]
        jumps += 1
    if i != len(nums) - 1:
        jumps += 1
    return jumps


print(jump([2, 3, 1, 1, 4]))
print(jump([2, 3, 0, 1, 4]))
print(jump([0]))
print(jump([2, 3, 1]))
print(jump([3, 2, 1, 0, 4]))
