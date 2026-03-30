def rotate(nums: list[int], k):
    # using two pointer approach
    ans = []
    start = len(nums) - k
    for i in range(start, len(nums)):
        ans.append(nums[i])

    for i in range(0, start):
        ans.append(nums[i])

    return ans


nums = [1, 2, 3, 4, 5, 6, 7]
nums2 = [-1, -100, 3, 99]


ans = rotate(nums2, 2)
print(ans)
