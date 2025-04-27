def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    resString = ''
    if numRows != 1:
        for j in range(0, len(s), numRows * 2 - 2):
            resString = resString + s[j]
        for i in range(1, numRows - 1):
            for j in range(i, len(s), numRows * 2 - 2):
                resString = resString + s[j]
                try:
                    resString = resString + s[j + (numRows - i) * 2 - 2]
                except Exception:
                    None
        for j in range(numRows - 1, len(s), numRows * 2 - 2):
            resString = resString + s[j]
        return resString
    else:
        return s


print(convert("PAYPALISHIRING", 3))
