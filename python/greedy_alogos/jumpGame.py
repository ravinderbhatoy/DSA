def canJump(nums: list[int]) -> bool:
    capacity = nums[0]

    for i in range(0, len(nums)):
        print(capacity, i)
        if capacity == 0 and nums[i] == 0 and i != len(nums) - 1:
            return False

        if capacity < nums[i]:
            capacity = nums[i]
        capacity -= 1

    return True


nums = [2, 0, 0]
print(canJump(nums))
