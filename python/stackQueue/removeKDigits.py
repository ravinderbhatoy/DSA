def removeKDigits(num: str, k: int) -> str:
    if len(num) == k or len(num) == k:
        return "0"

    stack = list()

    for ch in num:
        while len(stack) and k > 0 and int(stack[-1]) > int(ch):
            stack.pop()
            k -= 1

        stack.append(ch)

    # remove last digits if k is left
    while k and len(stack):
        k -= 1
        stack.pop()

    res = "".join(stack).lstrip('0')
    if not res:
        return "0"

    return res


num = "10200"
print(removeKDigits(num, 1))
