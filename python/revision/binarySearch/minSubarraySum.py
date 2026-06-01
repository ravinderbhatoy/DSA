def minSubArrayLen(target: int, nums: list[int]) -> int:
    left, right = 0, 0

    curr_sum = 0
    mini = float('inf')
    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum >= target:
            mini = min(mini, right - left + 1)
            curr_sum -= nums[left]
            left += 1
    return 0 if mini == float('inf') else mini


target = 7
nums = [2, 3, 1, 2, 4, 3]
print(minSubArrayLen(target, nums))
