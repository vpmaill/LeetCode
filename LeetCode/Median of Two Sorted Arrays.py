def findMedianSortedArrays(nums1, nums2):
    def median(nums):
        nums = sorted(nums)
        if len(nums) % 2 == 1:
            return nums[len(nums) // 2]
        else:
            return (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2

    tempList = nums1 + nums2
    return median(tempList)


print(findMedianSortedArrays([1, 2], [3]))
