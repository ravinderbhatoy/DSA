def numSubarrayWithSum(nums: list[int], goal: int) -> int:
    st = cnt = 0
    sum = 0

    for r in range(len(nums)):
        sum += nums[r]

    return cnt


nums = [1, 0, 1, 0, 1]
goal = 2
print(numSubarrayWithSum(nums, goal))
