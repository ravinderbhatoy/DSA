def isSorted(nums: list[int], n: int) -> bool:
    if n <= 1:
        return True
    return nums[n - 1] >= nums[n - 2] and isSorted(nums, n - 1)


nums = [1, 2, 3, 9, 5]
print(isSorted(nums, len(nums)))
