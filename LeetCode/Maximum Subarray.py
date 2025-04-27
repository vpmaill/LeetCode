def maxSubArray(nums):
    minin = nums[0]
    for i in nums:
        if i < 0:
            minin = max(minin, i)
            nums = nums[1:]
        else:
            break
    if len(nums) > 1:
        l = 0
        res = nums[0] if nums[0] > 0 else 0
        r = 1
        tempSum = res
        while r < len(nums):
            tempSum += nums[r]
            if tempSum > 0:
                res = max(res, tempSum)
            else:
                tempSum = 0
                l = r
            r += 1
        return res
    elif len(nums) == 1:
        return max(nums[0], minin)
    else:
        return minin


print(maxSubArray([-2, -1]))
