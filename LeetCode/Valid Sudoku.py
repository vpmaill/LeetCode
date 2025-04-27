def isValidSudoku(board):
    result = True
    checkCol = []
    for i in range(len(board)):
        checkCol.append([])
    for i in range(len(board)):
        tempCheckRow = []
        for j in range(len(board)):
            temp = board[i][j]
            if temp != ".":
                if (temp in checkCol[j]) or (temp in tempCheckRow):
                    result = False
                    break
                else:
                    checkCol[j].append(temp)
                    tempCheckRow.append(temp)
        if not result:
            break
    checkSquare = []
    for i in range(9):
        checkSquare.append([])
        for j in range(9):
            checkSquare[i].append([])
    for i in range(1, len(board), 3):
        for j in range(1, len(board), 3):
            for k in range(-1, 2):
                for m in range(-1, 2):
                    temp = board[i + k][j + m]
                    if temp != ".":
                        if temp in checkSquare[i][j]:
                            result = False
                        else:
                            checkSquare[i][j].append(temp)
    return result


print(isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                     [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                     ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                     [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

print(isValidSudoku([[".", ".", "4", ".", ".", ".", "6", "3", "."],
                     [".", ".", ".", ".", ".", ".", ".", ".", "."],
                     ["5", ".", ".", ".", ".", ".", ".", "9", "."],
                     [".", ".", ".", "5", "6", ".", ".", ".", "."],
                     ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
                     [".", ".", ".", "7", ".", ".", ".", ".", "."],
                     [".", ".", ".", "5", ".", ".", ".", ".", "."],
                     [".", ".", ".", ".", ".", ".", ".", ".", "."],
                     [".", ".", ".", ".", ".", ".", ".", ".", "."]]))
