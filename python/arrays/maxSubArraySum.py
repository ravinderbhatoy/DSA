def maxSum(nums: list[int]):
    maxi = float("-inf")
    for i in range(0, len(nums)):
        currSum = 0
        for j in range(i, len(nums)):
            currSum += nums[j]
            maxi = max(currSum, maxi)
    return maxi


def maxSum2(nums: list[int]):
    # using kadane's algorithm
    maxi = float("-inf")
    currSum = 0

    for num in nums:
        currSum += num
        maxi = max(currSum, maxi)
        if currSum < 0:
            currSum = 0

    return maxi


nums = [3, -4, 5, 4 - 1, 7, -8]
print(maxSum2(nums))
