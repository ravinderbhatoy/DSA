def getSubset(nums, ans, ind, all_subsets):
    if len(nums) == ind:
        all_subsets.append(ans[:])
        return

    ans.append(nums[ind])
    getSubset(nums, ans, ind + 1, all_subsets)
    ans.pop(-1)
    idx = ind + 1
    while idx < len(nums) and nums[idx] == nums[idx - 1]:
        idx += 1
    getSubset(nums, ans, ind + 1, all_subsets)


def subsetWithDup(nums: list[int]) -> list[list[int]]:
    ans = []
    ind = 0
    all_subsets = []
    nums = sorted(nums)
    getSubset(nums, ans, ind, all_subsets)
    return all_subsets


nums = [1, 2, 2]

print(subsetWithDup(nums))
