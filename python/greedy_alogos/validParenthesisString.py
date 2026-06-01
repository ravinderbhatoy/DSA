def checkValidString(s: str) -> bool:
    open_stack = []
    ast_stack = []

    for i, ch in enumerate(s):
        if ch == "*":
            ast_stack.append(i)
        elif ch == '(':
            open_stack.append(i)
        else:
            if open_stack:
                open_stack.pop()
            elif ast_stack:
                ast_stack.pop()
            else:
                return False

    while open_stack and ast_stack:
        if open_stack[-1] > ast_stack[-1]:
            # if asterisk comes from '(' this is invalid
            return False

        open_stack.pop()
        ast_stack.pop()

    return len(open_stack) == 0


s = "*(()*"
print(checkValidString(s))
