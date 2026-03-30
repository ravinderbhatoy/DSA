def fetchProductArray(nums):
    product = 1
    ans = [0] * len(nums)

    for ele in nums:
        product *= ele

    for i in range(0, len(nums)):
        ans[i] = product / nums[i]

    return ans


def fetchProductArray2(nums):
    ans = [0] * len(nums)

    for i in range(0, len(nums)):
        product = 1
        for j in range(0, len(nums)):
            if i != j:
                product *= nums[j]

        ans[i] = product

    return ans


print(fetchProductArray2([1, 2, 3, 4]))
