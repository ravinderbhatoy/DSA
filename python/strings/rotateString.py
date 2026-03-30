def isStringRotated(s: str, goal: str) -> bool:
    for i in range(0, len(s)):
        first = s[0]
        s = s[1:]
        s += first
        if s == goal:
            return True
    return False


s = "abcde"
goal = "eabcd"
print(isStringRotated(s, goal))
