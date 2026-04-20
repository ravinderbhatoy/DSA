def numberOfSubarrays(nums: list[int], goal: int) -> int:
    # the same of BinarySubarrayWithSum
    def countAtMost(k):
        if k < 0:
            return 0

        res = left = current_sum = 0
        for right in range(len(nums)):
            # Treat odd as 1 (count of odd numbers), even as 0
            current_sum += (nums[right] & 1)

            while current_sum > k:
                current_sum -= (nums[left] & 1)
                left += 1

            res += (right - left + 1)
        return res

    return countAtMost(goal) - countAtMost(goal - 1)


nums = [1, 1]
k = 2
print("output:", numberOfSubarrays(nums, k))
