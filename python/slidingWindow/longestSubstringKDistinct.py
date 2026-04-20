from collections import defaultdict


def kDistinctChars(k,  str) -> int:
    left = maxLen = 0
    hash = defaultdict(int)

    for right in range(len(str)):
        hash[str[right]] += 1

        while len(hash) > k:
            hash[str[left]] -= 1
            if hash[str[left]] == 0:
                del hash[str[left]]
            left += 1

        maxLen = max(maxLen, right - left + 1)

    return maxLen


str = "abbbbbbc"
k = 2

print(kDistinctChars(k, str))
