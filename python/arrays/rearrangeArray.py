def rearrangeArray(nums: list[int]) -> list[int]:
    ans = [0] * len(nums)
    posInd = 0
    negInd = 1

    for num in nums:
        if num > 0:
            ans[posInd] = num
            posInd += 2
        else:
            ans[negInd] = num
            negInd += 2
    return ans


nums = [-1, -2, -3, -4, 4, 3, 2, 1]
print(rearrangeArray(nums))
