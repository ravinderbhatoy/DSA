def myAtoi(s: str):
    mini = 2 ** 31 * -1
    maxi = 2 ** 31 - 1
    s = s.strip()
    if not s:
        return 0
    i = 0
    sign = 1
    if (s[i] == '-' or s[i] == '+'):
        sign = -1 if s[i] == '-' else 1
        i += 1
    num = 0

    def rec(i, num):
        if i >= len(s) or not s[i].isdigit():
            return num
        num = (num * 10) + int(s[i])
        if (num * sign < mini):
            return mini * sign
        if (num * sign > maxi):
            return maxi * sign
        return rec(i + 1, num)
    return rec(i, num) * sign


print(myAtoi("   -042"))
print(myAtoi("104"))
print(myAtoi("0-1"))
print(myAtoi("1337c0d3"))
print(myAtoi("10-4"))
print(myAtoi("-042"))
