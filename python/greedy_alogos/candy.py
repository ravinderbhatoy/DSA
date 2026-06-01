def candy(ratings: list[int]) -> int:
    sm = i = 1
    n = len(ratings)

    while i < n:
        if ratings[i] == ratings[i-1]:
            sm += 1
            i += 1
            continue

        peak = 1
        while i < n and ratings[i] > ratings[i-1]:
            peak += 1
            sm += peak
            i += 1
        down = 1
        while i < n and ratings[i] < ratings[i-1]:
            sm += down
            down += 1
            i += 1

        if down > peak:
            sm += down - peak

    return sm


ratings = [100, 80, 70, 60, 70, 80, 90, 100, 90, 80, 70, 60, 60]
print(candy(ratings))
