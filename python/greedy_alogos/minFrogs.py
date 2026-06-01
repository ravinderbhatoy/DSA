def minNumberOfFrogs(croakOfFrogs: str) -> int:
    c = r = o = a = k = 0
    activeFrogs = 0
    maxFrogs = 0

    for ch in croakOfFrogs:
        if ch == 'c':
            c += 1
            maxFrogs = max(maxFrogs, activeFrogs)
        elif ch == 'r':
            c -= 1
            r += 1
        elif ch == 'o':
            r -= 1
            o += 1
        elif ch == 'a':
            o -= 1
            a += 1
        elif ch == 'k':
            activeFrogs -= 1
            k += 1
            a -= 1

    if c < 0 or r < 0 or o < 0 or a < 0 or k < 0:
        return -1  # invalid frequencies

    return maxFrogs if activeFrogs == 0 else -1


croakOfFrogs = "croakcrook"
print(minNumberOfFrogs(croakOfFrogs))
