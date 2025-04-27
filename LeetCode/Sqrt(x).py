def mySqrt(x):
    for i in range(x // 2 + 2):
        if i * i <= x < (i + 1) * (i + 1):
            return i



print(mySqrt(1))
