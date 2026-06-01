def mergeIntervals(intervals: list[int]) -> list[int]:
    cnt = 1
    intervals = sorted(intervals, key=lambda x: x[1])
    prev = -1
    cnt = 0
    for interval in intervals:
        if interval[0] >= prev:
            cnt += 1
            prev = interval[1]

    return len(intervals) - cnt


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(mergeIntervals(intervals))
