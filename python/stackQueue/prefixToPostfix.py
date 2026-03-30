def prefixToPostfix(exp: str):
    stack = []

    for ch in exp[::-1]:
        if ch.isalpha():
            stack.append(ch)
        else:
            t1 = stack.pop()
            t2 = stack.pop()
            stack.append(t1+t2+ch)
    return stack.pop()


prefix = "/-AB*+DEF"
print(prefixToPostfix(prefix))
