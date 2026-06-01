def mergeIntervals(intervals: list[int]) -> list[int]:
    ans = []
    intervals = sorted(intervals)

    for interval in intervals:
        if not ans or ans[-1][1] < interval[0]:
            ans.append(interval)
        else:
            ans[-1][1] = max(ans[-1][1], interval[1])

    return ans


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(mergeIntervals(intervals))
