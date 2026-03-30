def largestOddNumber(num: str) -> str:
    end = len(num) - 1
    for i in range(end, -1, -1):
        value = int(num[i])
        if value % 2 != 0:
            return num[: i + 1]
    return ""


num = "16188"
print(largestOddNumber(num))
