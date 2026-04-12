def searchInsert(nums: list[int], target: int):
    low = 0
    high = len(nums) - 1
    pos = -1

    while (low <= high):
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return pos


nums = [1, 3, 5, 6]
target = 4

print(searchInsert(nums, target))
