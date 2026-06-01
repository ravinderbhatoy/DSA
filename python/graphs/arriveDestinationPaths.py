import heapq


def countPaths(n, roads: list[list[int]]) -> int:
    mod = int(1e9 + 7)
    adj = {i: [] for i in range(n)}
    for u, v, c in roads:
        # undirected
        adj[u].append([v, c])
        adj[v].append([u, c])

    dist = [float('inf')] * n
    src, dst = 0, n - 1
    dist[src] = 0  # distance from source

    pq = []
    ways = [0] * n  # no. of ways a node can be reached
    ways[src] = 1

    heapq.heappush(pq, [0, 0])

    while pq:
        cost, node = heapq.heappop(pq)
        for adjNode, ew in adj[node]:
            totalCost = cost + ew
            if totalCost == dist[adjNode]:
                ways[adjNode] = ways[adjNode] + ways[node]
            elif totalCost < dist[adjNode]:
                dist[adjNode] = totalCost
                ways[adjNode] = ways[node]
                heapq.heappush(pq, (totalCost, adjNode))

    return int(ways[dst] % mod)


n = 7
roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3],
         [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]
print(countPaths(n, roads))
