def longestConsecutive(nums: list[int]) -> int:
    myset = set(nums)
    longest = 1
    cnt = 0
    for num in myset:
        if (num - 1) not in myset:
            while num in myset:
                cnt += 1
                num += 1
        longest = max(longest, cnt)
    return longest


nums = [1, 0, 1, 2]
print(longestConsecutive(nums))
