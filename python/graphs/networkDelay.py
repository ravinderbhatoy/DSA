import heapq


def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
    # 1. Adjacency list (1-indexed)
    adj = {i: [] for i in range(1, n + 1)}
    for u, v, c in times:
        adj[u].append((v, c))

    # 2. Priority queue & distance tracking
    pq = []  # stores (cost, node)
    dist = [float('inf')] * (n + 1)
    dist[k] = 0

    heapq.heappush(pq, (0, k))

    while pq:
        cost, node = heapq.heappop(pq)

        # if we already found a shorter path to this node, skip it
        if cost > dist[node]:
            continue

        for adjNode, ew in adj[node]:
            if ew + cost < dist[adjNode]:
                dist[adjNode] = ew + cost
                heapq.heappush(pq, (ew + cost, adjNode))

    # 3. Find the maximum time taken to reach any node
    # We slice dist[1:] to ignore the 0th index dummy value
    max_time = max(dist[1:])

    return -1 if max_time == float('inf') else max_time


times = [[1, 2, 1], [1, 3, 4], [2, 3, 2], [4, 3, 1]]
n = 4
k = 1
print(networkDelayTime(times, n, k))
