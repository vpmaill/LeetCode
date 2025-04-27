def multiply(str1, str2):
    def convert(string):
        res = 0
        for i in string:
            tvalue = 0
            if i == '0':
                tvalue = 0
            elif i == '1':
                tvalue = 1
            elif i == '2':
                tvalue = 2
            elif i == '3':
                tvalue = 3
            elif i == '4':
                tvalue = 4
            elif i == '5':
                tvalue = 5
            elif i == '6':
                tvalue = 6
            elif i == '7':
                tvalue = 7
            elif i == '8':
                tvalue = 8
            elif i == '9':
                tvalue = 9
            res *= 10
            res += tvalue
        return res

    def backConvert(num):
        res = ""
        while num > 0:
            tvalue = ''
            i = num % 10
            num //= 10
            if i == 0:
                tvalue = '0'
            elif i == 1:
                tvalue = '1'
            elif i == 2:
                tvalue = '2'
            elif i == 3:
                tvalue = '3'
            elif i == 4:
                tvalue = '4'
            elif i == 5:
                tvalue = '5'
            elif i == 6:
                tvalue = '6'
            elif i == 7:
                tvalue = '7'
            elif i == 8:
                tvalue = '8'
            elif i == 9:
                tvalue = '9'
            res = tvalue + res
        if res == "":
            return "0"
        return res

    return backConvert(convert(str1) * convert(str2)), convert(str1), convert(str2)


print(multiply("0", "0"))
