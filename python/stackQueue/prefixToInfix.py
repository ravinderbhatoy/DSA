def prefixToInfix(exp: str):
    stack = []

    for ch in exp[::-1]:
        # Push operand into the stack
        if ch.isalpha() is True:
            print("Adding", ch)
            stack.append(ch)
        else:
            # pop last two operands and put operator between
            # them wrap around ()
            t1 = stack.pop()
            t2 = stack.pop()
            stack.append(t1+ch+t2)

    return stack.pop()


prefix = "*+PQ-MN"
print(prefixToInfix(prefix))
