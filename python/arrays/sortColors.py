def sortColors(nums: list[int]) -> None:
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            # if mid is 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# Dutch's national flag
# 0 -> low-1 (000...)
# low -> mid-1 (111...)
# mid -> high (210021...)
# high+1 -> n-1 (222....)

nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)
