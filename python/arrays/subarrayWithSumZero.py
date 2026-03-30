def longestSubarray(nums: list[int]) -> int:
    hashmap = dict()
    maxi = float("-inf")
    curr_sum = 0

    for i in range(len(nums)):
        curr_sum += nums[i]
        if curr_sum == 0:
            maxi = i + 1
        if hashmap.get(curr_sum) is not None:
            maxi = max(maxi, i - hashmap[curr_sum])
        else:
            hashmap[curr_sum] = i
    return maxi


nums = [15, -2, 2, -8, 1, 7, 10, 23]
print(longestSubarray(nums))
