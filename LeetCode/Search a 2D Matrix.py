def searchMatrix(matrix, target):
    for i in range(len(matrix)):
        if matrix[i][-1] >= target:
            j = 0
            while matrix[i][j] <= target:
                if matrix[i][j] == target:
                    return True
                j += 1
            return False
    return False


print(searchMatrix([[1]], 2))
