def checkSorted(nums: list[int]):
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return False
    return True


nums = [1, 2, 3, 7, 6]

print(checkSorted(nums))
