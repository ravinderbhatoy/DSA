import heapq


def spanningTree(V, edges: list[list[int]]):
    visited = [0] * V
    adj = {i: [] for i in range(V)}

    for u, v, w in edges:
        adj[u].append([v, w])
        adj[v].append([u, w])

    mst = []  # to store edges of MST
    mst_sum = 0  # spanning Tree sum
    pq = []  # (weight, node, parent)
    heapq.heappush(pq, [0, 0, -1])

    while pq:
        w, node, parent = heapq.heappop(pq)
        if visited[node]:
            continue

        visited[node] = 1
        mst_sum += w

        if parent != -1:
            mst.append([parent, node])

        for adjNode, ew in adj[node]:
            if not visited[adjNode]:
                heapq.heappush(pq, [ew, adjNode, node])

    return mst_sum


V = 3
edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]
output = spanningTree(V, edges)
print(output)
