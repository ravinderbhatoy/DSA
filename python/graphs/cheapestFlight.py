from queue import deque


def findCheapestPrice(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    adj = {i: [] for i in range(n)}

    for s, d, c in flights:
        adj[s].append([d, c])

    dist = [float('inf')] * n
    stops = 0

    dist[src] = 0
    que = deque([[stops, src, 0]])  # (stops, node, cost)

    while que:
        stops, node, cost = que.popleft()

        if stops > k:
            continue

        for adjNode, ew in adj[node]:
            if cost + ew < dist[adjNode] and stops <= k:
                dist[adjNode] = cost + ew
                que.append([stops + 1, adjNode, cost + ew])

    return -1 if dist[dst] == float('inf') else dist[dst]


n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1
print(findCheapestPrice(n, flights, src, dst, k))
