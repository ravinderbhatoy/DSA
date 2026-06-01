def insertInterval(intervals: list[list[int]],
                   newInterval: list[int]) -> list[list[int]]:
    # find the correct place for interval (binaryS (they are sorted))

    s, e = 0, len(intervals)

    while s < e:
        mid = (s + e) // 2
        if intervals[mid][0] < newInterval[0]:
            s = mid + 1
        else:
            e = mid

    intervals.insert(e, newInterval)

    merged = []

    for current in intervals:
        if not merged or merged[-1][1] < current[0]:
            merged.append(current)
        else:
            merged[-1][1] = max(merged[-1][1], current[1])

    return merged


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
print(insertInterval(intervals, newInterval))
