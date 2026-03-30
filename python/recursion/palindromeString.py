def palindromeRec(s: str, left, right):
    if left >= right:
        return True
    # skip if character is non alphanumeric (not letter or number)
    if not s[left].isalnum():
        return palindromeRec(s, left + 1, right)
    if not s[right].isalnum():
        return palindromeRec(s, left, right - 1)

    comparison = s[left].lower() == s[right].lower()
    return comparison and palindromeRec(s, left + 1, right - 1)


s = "A man, a plan, a canal: Panama"
print(palindromeRec(s, 0, len(s) - 1))
