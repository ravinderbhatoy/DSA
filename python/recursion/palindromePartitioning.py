def palindromePartioning(s: str):
    res = []

    def isPalindrome(s, start, end):
        while (start <= end):
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def backtrack(ind, sub: []):
        if ind == len(s):
            res.append(sub[:])
            return
        for i in range(ind, len(s)):
            if (isPalindrome(s, ind, i)):
                sub.append(s[ind: i+1])
                backtrack(i+1, sub)
                sub.pop()

    backtrack(0, [])
    return res


s = "aaa"
print(palindromePartioning(s))
