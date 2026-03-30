def findNCR(n: int, r: int) -> int:
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res / (i + 1)
    return res


def generateRow(n: int) -> list[int]:
    ans = [1]
    res = 1
    for i in range(1, n+1):
        res = res * (n - i)
        res = res / i
        ans.append(res)
    return ans


def generate(numRows: int) -> list[list[int]]:
    ans = [[1]]
    for i in range(0, numRows - 1):
        start, end = 0, 1
        row = [1]
        while end <= i:
            value = ans[i][start] + ans[i][end]
            row.append(value)
            start += 1
            end += 1
        row.append(1)
        ans.append(row)
    return ans


# print(generate(5))
print(generateRow(4))
