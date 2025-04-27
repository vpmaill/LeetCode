def setZeroes(matrix):
    row = []
    col = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                row.append(i)
                col.append(j)

    for i in range(len(matrix)):
        if i in row:
            matrix[i] = [0 for _ in range(len(matrix[i]))]
        for j in range(len(matrix[i])):
            if j in col:
                matrix[i][j] = 0


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
setZeroes(matrix)
print(matrix)
