def removeElement(nums, val):
    # remove all the elements = val
    left = 0
    right = len(nums) - 1

    while left <= right:
        if nums[left] == val:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1          # shrink valid range
        else:
            left += 1           # only move left if it's valid

    return left


nums = [2, 3]
val = 2
k = removeElement(nums, val)
print(sorted(nums[:k]))
