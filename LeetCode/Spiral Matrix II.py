def generateMatrix(n):
    matrix = [[1 for i in range(n)] for j in range(n)]
    num = 2
    rowNum = 0
    colNum = 0
    rowDif = 0
    colDif = 0
    direction = "right"
    if n == 1:
        return [[1]]
    while num <= n ** 2:
        if direction == "right":
            colNum += 1
            matrix[rowNum][colNum] = num
        elif direction == "down":
            rowNum += 1
            matrix[rowNum][colNum] = num
        elif direction == "left":
            colNum -= 1
            matrix[rowNum][colNum] = num
        elif direction == "up":
            rowNum -= 1
            matrix[rowNum][colNum] = num
        num += 1
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
    return matrix


print(generateMatrix(3))
