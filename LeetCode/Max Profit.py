def maxProfit(arr: list) -> int:
    left = 0
    right = len(arr) - 1
    curPair = [arr[left], arr[right]]
    tempMax = 0
    while left < right:
        if arr[right] - arr[left + 1] < arr[right - 1] - arr[left]:
            tempMax = max(tempMax, curPair[1] - arr[right - 1])
            right -= 1
            curPair[1] = max(arr[right], curPair[1])
        else:
            tempMax = max(tempMax, arr[left + 1] - curPair[0])
            left += 1
            curPair[0] = min(arr[left], curPair[0])
    return max(curPair[1] - curPair[0], tempMax)


print(maxProfit([0, 3, 8, 6, 8, 6, 6, 8, 2, 0, 2, 7]))
