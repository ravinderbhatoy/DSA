from collections import defaultdict


def getSubarrayBeauty(nums: list[int], k: int, x: int) -> list[int]:
    freq = defaultdict(int)
    ans = []

    for i, num in enumerate(nums):
        freq[num] += 1  # add incoming element

        if i >= k:
            old = nums[i - k]
            freq[old] -= 1
            if freq[old] == 0:
                del freq[old]

        if i >= k - 1:
            # find xth smallest negative
            count = 0
            for val in range(-50, 0):  # start from smallest
                count += freq[val]
                if count >= x:
                    ans.append(val)
                    break
            else:
                ans.append(0)  # fewer than x negatives
    return ans


nums = [1, -1, -3, -2, 3]
k = 3
x = 2

print(getSubarrayBeauty(nums, k, x))
