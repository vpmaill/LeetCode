def maxArea(height):
    right = len(height) - 1
    left = 0
    tempMax = 0
    while (left < right):
        tempMax = max(tempMax, min(height[right], height[left]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return tempMax