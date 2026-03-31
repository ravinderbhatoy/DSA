def minBitFlips(start, goal):
    num = start ^ goal
    ans = 0

    while num > 0:
        ans = ans + num & 1
        num = num >> 1

    return ans


print(minBitFlips(10, 7))
