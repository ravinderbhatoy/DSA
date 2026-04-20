def longestSubarrayWithSumK(nums: list[int], k: int) -> int:
    maxLen = 0
    left = 0
    total = 0

    for right in range(len(nums)):
        total += nums[right]

        while total > k:
            total -= nums[left]
            left += 1

        if total == k:
            maxLen = max(maxLen, right - left + 1)

    return maxLen


nums = [1, 2, 3, 1, 1, 1, 1]
k = 3
print(longestSubarrayWithSumK(nums, k))
