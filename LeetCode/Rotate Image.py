def rotate(matrix):
    n = len(matrix) - 1
    for k in range((len(matrix)) // 2):
        for i in range(n - 2 * k):
            matrix[0 + k][0 + i + k], matrix[0 + i + k][n - k], matrix[n - k][n - i - k], matrix[n - i - k][0 + k] = \
                matrix[n - i - k][0 + k], matrix[0 + k][0 + i + k], matrix[0 + i + k][n - k], matrix[n - k][n - i - k]
    return matrix


print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))
print(rotate([[24, 4, 38, 2, 21, 18, 33, 40], [24, 37, 25, 62, 37, 15, 35, 36], [42, 23, 13, 58, 17, 26, 19, 8],
              [32, 48, 9, 58, 36, 18, 40, 61], [23, 16, 0, 46, 35, 34, 23, 60], [9, 49, 60, 47, 1, 32, 20, 45],
              [56, 34, 40, 11, 61, 60, 20, 30], [45, 30, 25, 18, 49, 3, 16, 10]]))
