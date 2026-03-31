def convert2Binary(x: int):

    ans = ""
    while x > 1:
        ans = str(x % 2) + ans
        x = x // 2

    return str(x) + ans


def binary2Decimal(s: str):
    p2 = 0
    ans = 0
    for ch in s[::-1]:
        if ch == '1':
            ans = ans + pow(2, p2)
        p2 += 1
    return ans


binary = convert2Binary(13)
print(binary2Decimal(binary))
