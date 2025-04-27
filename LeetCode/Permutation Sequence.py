def getPermutation(n, k):
    num = [i + 1 for i in range(n)]

    def permute(nums):
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        backtrack(0)
        return result

    return "".join(list(map(str, sorted(permute(num))[k - 1])))


print(getPermutation(9, 136371))
