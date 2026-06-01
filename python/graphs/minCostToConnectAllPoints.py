import heapq


def minCostConnectPoints(points: list[list[int]]) -> int:
    V = len(points)
    visited = [0] * V
    adj = {i: [] for i in range(V)}

    for i in range(V):
        for j in range(i+1, V):
            weight = abs(points[i][0] - points[j][0]) + \
                abs(points[i][1] - points[j][1])

            adj[i].append([j, weight])
            adj[j].append([i, weight])

    pq = []
    mst_sum = 0
    heapq.heappush(pq, [0, 0])  # weight, node

    while pq:
        w, node = heapq.heappop(pq)

        if visited[node]:
            continue

        visited[node] = 1
        mst_sum += w

        for adjNode, ew in adj[node]:
            if not visited[adjNode]:
                heapq.heappush(pq, [ew, adjNode])

    return mst_sum


points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]

print(minCostConnectPoints(points))
