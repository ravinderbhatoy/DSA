def threeSum(nums: list[int]) -> list[list[int]]:
    ans = set()
    for i in range(len(nums)):
        st = set()
        for j in range(i + 1, len(nums)):
            tar = -(nums[i] + nums[j])
            if tar in st:
                triplet = tuple(sorted([tar, nums[i], nums[j]]))
                ans.add(triplet)
            st.add(nums[j])
    return [list(trio) for trio in ans]


def threeSumOptimal(nums: list[int]) -> list[list[int]]:
    ans = list()
    nums = sorted(nums)
    for i in range(0, len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            tar = nums[i] + nums[j] + nums[k]
            if tar > 0:
                k -= 1
            elif tar < 0:
                j += 1
            else:
                ans.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
    return ans


nums = [-1, 0, 1, 2, -1, -4]
print(threeSumOptimal(nums))
