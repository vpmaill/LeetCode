n = int(input())
nums = sorted(list(map(int, input().split())))
nums.insert(0, '0')
nums.append('0')
res = 0
for i in range(n):
    if nums[i + 1] != nums[i] and nums[i + 1] != nums[i + 2]:
        res += 1
print(res)

