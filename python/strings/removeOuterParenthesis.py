def removeOuterParenthesis(s: str) -> str:
    cnt = 0
    ans = ""
    for ch in s:
        if ch == ")":
            cnt -= 1
        if cnt != 0:
            ans += ch
        if ch == "(":
            cnt += 1
    return ans


s = "(()())(())(()(()))"
print(removeOuterParenthesis(s))
