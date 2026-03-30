def removeDuplicates(nums: list[int]) -> int:
    # one approach is to return set(nums) as set only contains unique elements
    uniqueIndex = 0
    uniqueValue = nums[0]
    for i in range(0, len(nums)):
        if nums[i] != uniqueValue:
            # we found a new unique
            uniqueValue = nums[i]
            nums[uniqueIndex + 1] = uniqueValue
            uniqueIndex += 1

    return uniqueIndex + 1


nums = [1, 2, 2, 4, 5, 6, 6]
k = removeDuplicates(nums)

print(nums[:k])
