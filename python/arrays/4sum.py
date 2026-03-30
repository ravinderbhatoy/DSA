def fourSum(nums: list[int], target) -> list[list[int]]:
    ans = list()
    nums = sorted(nums)

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums)):
            if j != i + 1 and nums[j] == nums[j - 1]:
                continue
            k = j + 1
            m = len(nums) - 1
            while k < m:
                total = nums[i] + nums[j] + nums[k] + nums[m]
                if total == target:
                    ans.append([nums[i], nums[j], nums[k], nums[m]])
                    k += 1
                    m -= 1
                    while k < m and nums[k] == nums[k - 1]:
                        k += 1
                    while k < m and nums[m] == nums[m + 1]:
                        m -= 1
                elif total > target:
                    m -= 1
                else:
                    k += 1
    return ans


nums = [-2, -1, 0, 0, 1, 2]
target = 0

print(fourSum(nums, target))
