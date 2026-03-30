def sortArray(nums: list) -> list:
    mid = 0
    low = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            mid += 1
            low += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums


nums = [2, 0, 2, 1, 1, 0, 1, 2, 0, 0]

print(sortArray(nums))
