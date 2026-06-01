def findDuplicate(nums: list[int]) -> int:
    for num in nums:
        print(nums)
        num = abs(num)
        if nums[num] < 0:
            return num
        nums[num] *= -1
    return -1


nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))
