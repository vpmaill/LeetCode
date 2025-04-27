def intToRoman(num):
    res = ''
    res = res + num // 1000 * "M"
    num %= 1000
    if num // 100 == 9:
        res = res + "CM"
    elif num // 100 > 4:
        res = res + "D" + (num // 100) % 5 * "C"
    elif num // 100 == 4:
        res = res + "CD"
    else:
        res = res + "C" * (num // 100)
    num %= 100
    if num // 10 == 9:
        res = res + "XC"
    elif num // 10 > 4:
        res = res + "L" + (num // 10) % 5 * "X"
    elif num // 10 == 4:
        res = res + "XL"
    else:
        res = res + "X" * (num // 10)
    num %= 10
    if num == 9:
        res = res + "IX"
    elif num > 4:
        res = res + "V" + num % 5 * "I"
    elif num == 4:
        res = res + "IV"
    else:
        res = res + "I" * num
    return res