def postfixToPrefix(exp: str):
    stack = []

    for ch in exp:
        if ch.isalpha():
            stack.append(ch)
        else:
            t1 = stack.pop()
            t2 = stack.pop()
            stack.append(ch+t2+t1)

    return stack.pop()


postfix = "AB-DE+F*/"
print(postfixToPrefix(postfix))
