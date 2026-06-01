def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    ans = 0
    i = 0
    product = 1

    for j in range(len(nums)):
        product *= nums[j]
        while product >= k and i <= j:
            product //= nums[i]
            i += 1
        ans = ans + (j - i + 1)

    return ans


nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
k = 1000
print(len(nums))

print("output:", numSubarrayProductLessThanK(nums, k))
