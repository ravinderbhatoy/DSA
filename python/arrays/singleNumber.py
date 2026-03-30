def singleNumber(nums: list[int]) -> int:
    xor = 0
    for num in nums:
        xor ^= num
    return xor


print(singleNumber([4, 1, 2, 2, 1]))
