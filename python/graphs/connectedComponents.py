from collections import defaultdict


def countCompleteComponents(n: int, edges: list[list[int]]) -> int:
    adjList = defaultdict(list)
    complete_count = 0

    for u, v in edges:
        adjList[u].append(v)
        adjList[v].append(u)

    visited = [False] * n

    def dfs(u, neighbours):
        nonlocal visited, adjList
        visited[u] = True
        neighbours.append(u)

        for v in adjList[u]:
            if not visited[v]:
                dfs(v, neighbours)

    for i in range(n):
        if not visited[i]:
            neighbours = []
            dfs(i, neighbours)

            k = len(neighbours)
            fully_connected = True

            for node in neighbours:
                if len(adjList[node]) != k - 1:
                    fully_connected = False
                    break

            if fully_connected:
                complete_count += 1

    return complete_count


n = 6
edges = [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]
print(countCompleteComponents(n, edges))
