def letterCombinations(digits):
    values = {2: ["a", "b", "c"],
              3: ["d", "e", "f"],
              4: ["g", "h", "i"],
              5: ["j", "k", "l"],
              6: ["m", "n", "o"],
              7: ["p", "q", "r", "s"],
              8: ["t", "u", "v"],
              9: ["w", "x", "y", "z"]}
    if digits == "":
        return []
    resList = [""]
    for i in digits:
        tempList = []
        for j in values[int(i)]:
            for k in range(len(resList)):
                tempList.append(resList[k] + j)
        resList = tempList
    return resList


print(letterCombinations("2"))
