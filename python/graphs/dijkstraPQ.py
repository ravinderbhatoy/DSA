from queue import PriorityQueue


def dijkstra(V, edges, src):
    adj = {i: [] for i in range(V)}

    for u, v, w in edges:
        adj[u].append((v, w))
        # undirected graph
        adj[v].append((u, w))

    distance = [float('inf')] * V

    pq = PriorityQueue()  # (weight, node)
    pq.put((0, src))
    distance[src] = 0

    while not pq.empty():
        edge_weight, node = pq.get()

        for adjNode, w in adj[node]:
            t_distance = edge_weight + w
            if (t_distance < distance[adjNode]):
                distance[adjNode] = t_distance
                pq.put((t_distance, adjNode))

    return distance


V = 3
e = 3
edges = [[0, 1, 1],
         [1, 2, 3],
         [0, 2, 6]]

print(dijkstra(V, edges, 0))
