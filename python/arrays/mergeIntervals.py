def mergeIntervals(intervals: list[list[int]]) -> list[list[int]]:
    ans = list()
    intervals = sorted(intervals)
    for i in range(0, len(intervals)):
        if not len(ans) or intervals[i][0] > ans[-1][1]:
            ans.append(intervals[i])
        else:
            ans[-1][1] = max(ans[-1][1], intervals[i][1])
    return ans


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(mergeIntervals(intervals))
