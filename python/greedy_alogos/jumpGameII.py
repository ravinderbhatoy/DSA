def canJump(nums: list[int]) -> bool:
    capacity = nums[0]
    maxi = -1
    refil = 1

    for i in range(0, len(nums)):
        maxi = max(nums[i], maxi)
        if capacity == 0 and i < len(nums) - 1:
            capacity = maxi
            refil += 1
        capacity -= 1
        maxi -= 1

    return refil


nums = [8, 4, 5, 10, 20, 4, 3, 1]
print(canJump(nums))
