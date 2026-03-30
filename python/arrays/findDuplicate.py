def findDuplicate(nums: list[int]) -> int:
    ans = 0
    for num in nums:
        ans = ans ^ num
    return ans


nums = [1, 2, 3, 3, 5]
print(findDuplicate(nums))
