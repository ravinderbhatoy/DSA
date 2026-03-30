def search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid

        elif mid < len(nums) - 1 and nums[mid] > nums[mid + 1] or mid > 0 and nums[mid] < nums[mid - 1]:
            if nums[mid] > target:
                low = mid + 1
            else:
                high = mid - 1

        else:
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

    return -1


nums = [1]
print(search(nums, 0))
