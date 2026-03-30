def reverseWords(s: str) -> str:
    ans = ""
    start = 0
    while start < len(s):
        space = start
        word = ""
        while space < len(s) and s[space] != " ":
            word += s[space]
            space += 1
        start = space + 1
        if word:
            ans = word + " " + ans
    return ans[:-1]


s = "  Cute you   are"
print(reverseWords(s))
