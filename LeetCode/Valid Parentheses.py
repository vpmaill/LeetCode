def isValid(s):
    i = 0
    n = len(s)
    while i < n - 1:
        if s[i] + s[i + 1] == "[]" or s[i] + s[i + 1] == "()" or s[i] + s[i + 1] == "{}":
            s = s[:i] + s[i + 2:]
            n -= 2
            i = 0
        else:
            i += 1
    if s == "":
        return True
    return False
