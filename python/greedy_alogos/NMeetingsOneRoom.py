def assignMeetings(start: list[int], end: list[int]) -> int:
    timings = [(s, e) for s, e in zip(start, end)]

    timings = sorted(timings, key=lambda x: x[1])
    freeTime = -1

    ans = 0

    for s, e in timings:
        if freeTime < s:
            ans += 1
            freeTime = e

    return ans


start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]
print(assignMeetings(start, end))
