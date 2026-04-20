def numSubarrayWithSum(nums: list[int], goal: int) -> int:
    def countSubarrays(nums, goal):
        if goal < 0:
            return 0
        sum = left = cnt = 0

        for right in range(len(nums)):
            sum += nums[right]

            while sum > goal:
                sum -= nums[left]
                left += 1

            cnt += (right - left) + 1
        return cnt

    return countSubarrays(nums, goal) - countSubarrays(nums, goal - 1)


nums = [0, 0, 0, 0, 0]
goal = 0
print(numSubarrayWithSum(nums, goal))
