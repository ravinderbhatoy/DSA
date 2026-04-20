def maximumSubarraySum(nums: list[int], k: int) -> int:
    maxSum = 0
    prev_idx = {}
    l = curr_sum = 0

    for r in range(len(nums)):
        curr_sum += nums[r]
        i = prev_idx.get(nums[r], -1)

        while l <= i or r - l + 1 > k:
            curr_sum -= nums[l]
            l += 1

        if r - l + 1 == k:
            maxSum = max(maxSum, curr_sum)

        prev_idx[nums[r]] = r

    return maxSum


nums = [1, 5, 4, 2, 9, 9, 9]
k = 3

print(maximumSubarraySum(nums, k))
