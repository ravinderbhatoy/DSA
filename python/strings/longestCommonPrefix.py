def longestCommonPrefix(strs):
    ans = ""
    if len(strs) == 1:
        return strs[0]
    for i in range(len(strs[0])):
        print(f"Checking for {strs[0][i]}")
        for j in range(1, len(strs)):
            if i > len(strs[j]):
                return ans
            if strs[0][i] != strs[j][i]:
                return ans
        ans += strs[0][i]
    return ans


# O(m x n)
# m -> no. of character is first string
# n -> length of strs

strs = ["ab", "a"]
print(longestCommonPrefix(strs))
