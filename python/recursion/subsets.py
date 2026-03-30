def printSubsets(nums: list[int], ans: list[int], i: int,
                 res: list[int]) -> None:
    if i == len(nums):
        res.append(ans[:])
        return
    # include
    ans.append(nums[i])
    printSubsets(nums, ans, i + 1, res)

    ans.pop(-1)
    # exclude
    printSubsets(nums, ans, i + 1, res)


nums = [2, 3, 1]
res = []
printSubsets(nums, [], 0, res)
print(res)
