def sortColors(nums):
    nums[:] = [0 for _ in range(nums.count(0))] + [1 for _ in range(nums.count(1))] + [2 for _ in range(nums.count(2))]


nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)
