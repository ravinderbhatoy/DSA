def findContentChildren(g: list[int], s: list[int]) -> int:
    ans = 0

    g = sorted(g)
    s = sorted(s)

    child = 0
    cookie = 0

    while child < len(g) and cookie < len(s):
        if g[child] <= s[cookie]:
            ans += 1
            child += 1
            cookie += 1
        elif g[child] > s[cookie]:
            cookie += 1

    return ans
