def spiralOrder(matrix):
    res = [matrix[0][0]]
    rowNum = 0
    colNum = 0
    rowDif = 0
    colDif = 0
    direction = "right"
    if len(matrix) == 1:
        return matrix[0]
    if len(matrix[0]) == 1:
        for i in matrix[1:]:
            res.append(i[0])
        return res
    while len(res) < (len(matrix) * len(matrix[0])):
        if direction == "right":
            colNum += 1
            res.append(matrix[rowNum][colNum])
        elif direction == "down":
            rowNum += 1
            res.append(matrix[rowNum][colNum])
        elif direction == "left":
            colNum -= 1
            res.append(matrix[rowNum][colNum])
        elif direction == "up":
            rowNum -= 1
            res.append(matrix[rowNum][colNum])
        if colNum == len(matrix[0]) - 1 - colDif and rowNum - rowDif == 0:
            direction = "down"
        elif colNum - colDif == 0 and rowNum - rowDif == 0:
            if direction != "right":
                direction = "right"
                colDif += 1
        elif colNum == len(matrix[0]) - 1 - colDif and rowNum == len(matrix) - 1 - rowDif:
            direction = "left"
        elif colNum - colDif == 0 and rowNum == len(matrix) - 1 - rowDif:
            if direction != "up":
                direction = "up"
                rowDif += 1
    return res


print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(spiralOrder([[3], [2]]))
print(spiralOrder([[1]]))
print(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]))
print(spiralOrder([[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13]]))
