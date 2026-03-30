def isValid(s: str) -> bool:
    chars = list()
    # 0 or 1 can't be a valid paretheis
    if len(s) == 1:
        return False

    for p in s:
        if p == '(' or p == '{' or p == '[':
            chars.append(p)
        else:
            if not len(chars):
                # starting with the closing
                return False
            if p == ')' and chars[-1] != '(':
                return False
            elif p == ']' and chars[-1] != '[':
                print("]")
                return False
            elif p == '}' and chars[-1] != '{':
                print("}")
                return False
            chars.pop()
    return True


s = "([])"
print(isValid(s))
