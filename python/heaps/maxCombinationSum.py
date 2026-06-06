import heapq


def topKsumPairs(a: list[int], b: list[int], k):
    a.sort(reverse=True)
    b.sort(reverse=True)

    ans = []
    pq = []  # maxHeap (value, pair(x, y))

    # x and y represents indices
    x = y = 0

    value = -(a[x] + b[y])  # negative to treat as max
    heapq.heappush(pq, (value, (x, y)))  # value, x, y
    visted = set((x, y))  # keep only unique pairs

    while k > 0:
        val, indexes = heapq.heappop(pq)
        x, y = indexes
        ans.append(-val)

        if x + 1 < len(a) and (x+1, y) not in visted:
            value = -(a[x + 1] + b[y])
            heapq.heappush(pq, (value, (x + 1, y)))
            visted.add((x + 1, y))

        if y + 1 < len(b) and (x, y + 1) not in visted:
            value = -(a[x] + b[y+1])
            heapq.heappush(pq, (value, (x, y+1)))
            visted.add((x, y + 1))

        k -= 1

    return ans


a = [3, 2]
b = [1, 4]
k = 2

print(topKsumPairs(a, b, k))
