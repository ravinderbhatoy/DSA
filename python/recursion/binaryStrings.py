def binaryString(n: int) -> list[str]:
    res = []

    def backtrack(curStr):
        if len(curStr) == n:
            res.append(curStr)
            return

        if not curStr or curStr and curStr[-1] != "1":
            backtrack(curStr + "1")
        backtrack(curStr + "0")

    backtrack(0, "")
    return res


n = 3
print(binaryString(n))
