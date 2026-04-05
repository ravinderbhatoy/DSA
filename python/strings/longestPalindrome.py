def longestPalindrome(s):
    def fetchPalindrome(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return left+1, right - left - 1

    maxStart = 0
    maxLen = 0
    for i in range(len(s)):
        # odd comparison
        start1, len1 = fetchPalindrome(s, i, i)
        if len1 > maxLen:
            maxStart, maxLen = start1, len1

        # even  comparison
        start2, len2 = fetchPalindrome(s, i, i + 1)
        if len2 > maxLen:
            maxStart, maxLen = start2, len2

    return s[maxStart: maxStart + maxLen]


s = "cbbd"
print(longestPalindrome(s))
