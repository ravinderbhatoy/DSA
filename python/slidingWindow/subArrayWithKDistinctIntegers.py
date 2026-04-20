from collections import defaultdict


def subarrayWithKDistinct(nums: list[int], k: int) -> int:
    """
    Find out no. of subarrays with distinct integers <= k
    and also <= k - 1 subtract them (cnt(k) - cnt(k - 1))
    """
    def countFreq(nums, target):
        if target < 0:
            return 0

        left = res = 0
        hash = defaultdict(int)

        for right in range(len(nums)):
            hash[nums[right]] += 1

            while len(hash) > target:
                hash[nums[left]] -= 1
                if hash[nums[left]] == 0:
                    del hash[nums[left]]
                left += 1

            res += (right - left) + 1
        return res

    return countFreq(nums, k) - countFreq(nums, k-1)


nums = [1, 2, 1, 2, 3]
k = 2

print(subarrayWithKDistinct(nums, k))
