def isIsoMorphic(s, t) -> bool:
    m1 = [0] * 256
    m2 = [0] * 256

    n = len(s)

    for i in range(n):
        if m1[ord(s[i])] != m2[ord(t[i])]:
            return False
        m1[ord(s[i])] = i + 1
        m2[ord(t[i])] = i + 1
    return True


s = "foo"
t = "baa"
print(isIsoMorphic(s, t))
