def lengthOfLongestSubstring(s: str) -> int:
    maxCount = 0
    n = len(s)
    for i in range(n):
        # We need a new hashmap for every starting position
        hashmap = {}
        curr_cnt = 0

        for j in range(i, n):
            # If we see a character again, this substring is invalid
            if s[j] in hashmap:
                break

            # Otherwise, add to hashmap and update count
            hashmap[s[j]] = 1
            curr_cnt += 1

            # Update maxCount after adding a valid character
            maxCount = max(maxCount, curr_cnt)

    return maxCount


s = "pwwkew"

print(lengthOfLongestSubstring(s))
