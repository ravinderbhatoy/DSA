def postfixToInfix(exp: str):
    stack = []

    for ch in exp:
        # Push operand into the stack
        if ch.isalpha() is True:
            print("Adding", ch)
            stack.append(ch)
        else:
            # pop last two operands and put operator between
            # them wrap around ()
            t1 = stack.pop()
            t2 = stack.pop()
            stack.append(t2+ch+t1)

    return stack.pop()


postfix = "AB-DE+F*/"
print(postfixToInfix(postfix))
