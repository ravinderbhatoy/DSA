def maxProduct(nums):
    maxi = float("-inf")
    prefix = 1
    suffix = 1
    size = len(nums)

    for i in range(len(nums)):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1
        prefix *= nums[i]
        suffix *= nums[size - i - 1]
        maxi = max(maxi, max(prefix, suffix))

    return maxi


nums = [-2, 0, -1]
print(maxProduct(nums))
