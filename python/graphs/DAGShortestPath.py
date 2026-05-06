def shortestPath(V: int, E: int, edges: list[list[int]]) -> list[int]:
    adjacency = {i: [] for i in range(V)}
    src = 0

    for u, v, w in edges:
        adjacency[u].append((v,  w))

    visited = [0] * V
    stack = []
    # topo sort

    def topoSort(node):
        visited[node] = 1

        for adj, w in adjacency[node]:
            if not visited[adj]:
                topoSort(adj)

        stack.append(node)

    for i in range(V):
        if not visited[i]:
            topoSort(src)

    distance = [float("inf")] * V
    # source node distance
    distance[src] = 0

    while stack:
        node = stack.pop()
        for adj, w in adjacency[node]:
            curr_w = distance[node] + w
            if curr_w < distance[adj]:
                distance[adj] = curr_w

    for i in range(V):
        if distance[i] == float('inf'):
            distance[i] = -1

    return distance


V = 6
E = 7
edges = [
    [0, 1, 2],
    [0, 4, 1],
    [4, 5, 4],
    [4, 2, 2],
    [1, 2, 3],
    [2, 3, 6],
    [5, 3, 1]
]

print(shortestPath(V, E, edges))
