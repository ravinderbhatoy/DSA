def findMaxConsecutiveOnes(nums: list[int]) -> int:
    count = 0
    maxCount = -1
    for num in nums:
        if num == 1:
            count += 1
            maxCount = max(count, maxCount)
        else:
            count = 0
    return maxCount


nums = [1, 0, 1, 1, 0, 1]
print(findMaxConsecutiveOnes(nums))
