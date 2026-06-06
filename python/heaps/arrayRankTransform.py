import heapq


def arrayRankTransform(arr: list[int]) -> list[int]:
    pq = []
    ans = [0] * len(arr)

    for i in range(len(arr)):
        heapq.heappush(pq, (arr[i], i))

    cnt = 0
    prev = None

    while pq:
        val, i = heapq.heappop(pq)
        if val != prev:
            cnt += 1
        ans[i] = cnt
        prev = val

    return ans


arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
arr = [100, 100, 100]
arr = []
print(arrayRankTransform(arr))
