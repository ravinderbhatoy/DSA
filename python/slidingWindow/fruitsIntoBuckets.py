from collections import defaultdict


def totalFruits(fruits: list[int]) -> int:
    maxCount = 0
    freqMap = defaultdict(int)
    s = 0

    for e in range(len(fruits)):
        freqMap[fruits[e]] += 1

        while len(freqMap) > 2:
            freqMap[fruits[s]] -= 1
            if freqMap[fruits[s]] == 0:
                del freqMap[fruits[s]]
            s += 1
        if len(freqMap) <= 2:
            maxCount = max(maxCount, e-s + 1)
    return maxCount


fruits = [0, 1, 2, 2]
print(totalFruits(fruits))
