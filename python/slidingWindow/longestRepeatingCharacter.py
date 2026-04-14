def characterReplacement(s: str, k: int) -> int:

    maxFreq = maxLen = st = 0
    hashMap = [0] * 26

    for e in range(len(s)):
        ind = ord(s[e]) - ord('A')
        hashMap[ind] += 1
        maxFreq = max(maxFreq, hashMap[ind])

        if ((e - st + 1) - maxFreq > k):
            ind = ord(s[st]) - ord('A')
            hashMap[ind] -= 1
            st += 1
        if ((e - st + 1) - maxFreq <= k):
            maxLen = max(maxLen, e - st + 1)

    return maxLen


s = "AAABBCCD"
k = 2

print(characterReplacement(s, k))
