from collections import defaultdict


def minWindow(s: str, t: str) -> str:
    minLen = float('inf')
    n = len(s)
    m = len(t)
    sIndex = -1
    left = 0
    cnt = 0

    hashmap = defaultdict(int)

    for i in range(m):
        hashmap[t[i]] += 1

    for right in range(n):
        if hashmap[s[right]] > 0:
            cnt += 1

        hashmap[s[right]] -= 1

        while cnt == m:
            if right - left + 1 < minLen:
                minLen = right - left + 1
                sIndex = left
            hashmap[s[left]] += 1
            if hashmap[s[left]] > 0:
                cnt -= 1
            left += 1

    if minLen == float('inf'):
        return ""
    return s[sIndex: sIndex + minLen]


s = "cabwefgewcwaefgcf"
t = "cae"

print(minWindow(s, t))
