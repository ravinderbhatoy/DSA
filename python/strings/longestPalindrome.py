def longestPalindrome(s):

    def fetchPalindrome(s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if left == right:
                count += 1
            else:
                count += 2

            left -= 1
            right += 1

        return s[left: count - 1]

    output = ""
    maxCount = 0
    for i in range(len(s)):
        # odd comparison
        ans = fetchPalindrome(s, i, i)
        if len(ans) > maxCount:
            output = ans
            maxCount = len(ans)

        # even comparison
        ans = fetchPalindrome(s, i, i + 1)
        if len(ans) > maxCount:
            output = ans
            maxCount = len(ans)

    return output


s = "cbbd"
print(longestPalindrome(s))
