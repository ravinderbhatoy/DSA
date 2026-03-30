def subArraySum(nums: [int], k):
    count = 0
    curr_sum = 0
    prefixSum = {0: 1}

    for i in range(0, len(nums)):
        curr_sum += nums[i]
        count += prefixSum.get(curr_sum - k, 0)
        prefixSum[curr_sum] = prefixSum.get(curr_sum, 0) + 1
    return count


nums = [0, 0, 0]
k = 0

print(subArraySum(nums, k))
