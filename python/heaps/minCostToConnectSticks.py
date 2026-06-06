import heapq


def minimumCostToConnectSticks(arr):
    minHeap = arr
    heapq.heapify(minHeap)

    res = 0

    while len(minHeap) > 1:
        diff = heapq.heappop(minHeap) + heapq.heappop(minHeap)
        res += diff

        heapq.heappush(minHeap, diff)

    return res


arr = [2, 9, 7]
print(minimumCostToConnectSticks(arr))
