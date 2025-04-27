def plusOne(digits):
    res = 0
    for i in digits:
        res *= 10
        res += i
    return list(map(int, list(str(res + 1))))


print(plusOne([1, 2, 9]))
