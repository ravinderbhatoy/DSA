def lcs(s, t):
    mapA = dict()
    mapB = dict()
    ans = ""

    for i in range(len(s)):
        mapA[s[i]] = i

    for i in range(len(t)):
        mapB[t[i]] = i

    for key in mapA.keys():
        if mapB.get(key) is None:
            continue

        if not ans:
            ans += key
        elif mapB[key] > mapB[ans[-1]]:
            ans += key

    return ans


s = "abcdb"
t = "bcacdhb"

print(lcs(s, t))
