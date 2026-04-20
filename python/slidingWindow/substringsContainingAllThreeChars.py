def numberOfSubstrings(s: str) -> int:
    res = 0
    mpp = {}
    for i in range(len(s)):
        mpp[s[i]] = i

    if len(mpp) == 3:
        res = res + min([mpp['a'], mpp['b'], mpp['c']]) + 1

    return res


s = "abcabc"
print(numberOfSubstrings(s))
