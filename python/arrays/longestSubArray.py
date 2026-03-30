def longestSubArrayWithSumK(a: [int], k: int) -> int:
    preSum = dict()
    sum = 0
    maxLen = 0

    for i in range(0, len(a)):
        sum += a[i]
        if sum == k:
            maxLen = i + 1
        rem = sum - k
        if preSum.get(rem) is not None:
            length = i - preSum[rem]
            maxLen = max(length, maxLen)
        if preSum.get(sum) is None:
            preSum[sum] = i
    return maxLen


def longestSubArrayWithSumKPositives(nums: [int], k):
    # two pointer approach
    right = 0
    left = 0
    sum = nums[right]
    maxLen = 0

    while right < len(nums):
        while left < right and sum > k:
            sum -= nums[left]
            left += 1
        if sum == k:
            maxLen = max(maxLen, right - left + 1)
        right += 1
        if right < len(nums):
            sum += nums[right]

    return maxLen


nums = [1, 2, 3, 1, 1, 1]
k = 3

print(longestSubArrayWithSumKPositives(nums, k))
