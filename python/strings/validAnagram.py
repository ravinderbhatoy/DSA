def isAnagram(s: str, t: str) -> bool:
    m1 = [0] * 26
    m2 = [0] * 26

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        m1[122 - ord(s[i])] += 1
        m2[122 - ord(t[i])] += 1

    for i in range(len(t)):
        val1 = m1[122 - ord(s[i])]
        val2 = m2[122 - ord(s[i])]

        if val1 != val2:
            return False

    return True
