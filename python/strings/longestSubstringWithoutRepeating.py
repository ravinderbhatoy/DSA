def lengthOfLongestSubstring(s):
    if not s:
        return 0

    left = right = 0
    hashmap = dict()
    maxlen = 0

    while right < len(s):
        if hashmap.get(s[right], -1) >= left:
            left = hashmap[s[right]] + 1
        maxlen = max(maxlen, right - left + 1)
        hashmap[s[right]] = right
        right += 1

    return maxlen


s = "au"
print(lengthOfLongestSubstring(s))
