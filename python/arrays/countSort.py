def countSort(nums):
    maxi = max(nums)
    freq = [0] * (maxi + 1)

    for num in nums:
        freq[num] += 1

    for i in range(1, len(freq)):
        freq[i] += freq[i-1]

    ans = [0] * len(nums)

    for i in range(len(nums)):
        ans[freq[nums[i]] - 1] = nums[i]
        freq[nums[i]] -= 1

    print(ans)

    nums[:] = ans[:]


nums = [0, 1, 2, 0, 3, 3, 4]
countSort(nums)
print(nums)
