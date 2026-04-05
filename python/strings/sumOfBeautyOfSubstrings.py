from collections import Counter


def beautySum(s: str) -> int:
    sm = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            myCounter = Counter(s[i:j+1])
            sm = sm + (myCounter.most_common()
                       [0][1] - myCounter.most_common()[-1][1])

    return sm


s = "aabcb"
print(beautySum(s))
