from collections import defaultdict, deque


def shortestPath(V, edges, src):
    adjacencyList = defaultdict(list)
    for u, v in edges:
        adjacencyList[u].append(v)
        adjacencyList[v].append(u)

    paths = [float('inf')] * V
    queue = deque([(src, 0)])  # (node, weight)
    paths[src] = 0

    while queue:
        n, w = queue.popleft()
        w += 1
        for nei in adjacencyList[n]:
            if w < paths[nei]:
                paths[nei] = w
                queue.append((nei, w))

    return paths


V = 9
E = 10
edges = [[0, 1], [0, 3], [1, 2], [3, 4], [4, 5],
         [2, 6], [5, 6], [6, 7], [6, 8], [7, 8]]
src = 0

print(shortestPath(V, edges, src))
