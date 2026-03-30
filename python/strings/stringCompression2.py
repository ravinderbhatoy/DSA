def getCompressedString(s):
    count = 1
    res = []
    i = 0
    while i < len(s):
        char = s[i]
        count = 0

        while i < len(s) and s[i] == char:
            count += 1
            i += 1

        res.append(char)
        if count > 1:
            res.append(str(count))

    return "".join(res)


s = "aaaabcc"
print(getCompressedString(s))
