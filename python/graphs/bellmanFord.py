def bellmanFord(V, edges, src):
    dist = [1e8] * V
    dist[src] = 0

    for _ in range(V):
        for u, v, w in edges:
            if (dist[u] != 1e8 and dist[u] + w < dist[v]):
                dist[v] = dist[u] + w

    # detect for negative cycles
    for u, v, w in edges:
        if (dist[u] != 1e8 and dist[u] + w < dist[v]):
            return [-1]

    return dist
