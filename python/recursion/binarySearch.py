def recBs(nums: list[int], target, low, high):
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return recBs(nums, target, low, mid - 1)
    else:
        return recBs(nums, target, mid + 1, high)


def bs(nums: list[int], target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1


nums = [-1, 0, 3, 5, 7, 9]
target = 3
low = 0
high = len(nums) - 1
print(recBs(nums, target, low, high))
