from collections import defaultdict


def topKFrequent(nums: list[int], k: int):
    # count -> [values]
    freq = [[] for i in range(len(nums) + 1)]
    hashmap = defaultdict(int)

    # count frequencies
    for num in nums:
        hashmap[num] += 1

    # map them in frequency list
    for n, c in hashmap.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

    return res


nums = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
k = 2

print(topKFrequent(nums, k))
