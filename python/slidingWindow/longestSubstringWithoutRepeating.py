def lengthOfLongestSubstring(s: str) -> int:
    maxLen = st = 0

    hash = [-1] * 256  # max characters

    for e in range(len(s)):
        if hash[ord(s[e])] >= st:
            st = hash[ord(s[e])] + 1

        hash[ord(s[e])] = e
        maxLen = max(maxLen, e - st + 1)

    return maxLen


s = "pwwkew"

print(lengthOfLongestSubstring(s))
