def isBipartite(graph: list[list[int]]) -> bool:
    colors = [None] * len(graph)

    def dfs(node, c) -> bool:
        colors[node] = c

        for adj in graph[node]:
            if colors[adj] is None:
                if not dfs(adj, not c):
                    return False
            elif colors[adj] == c:
                return False

        return True

    for i in range(len(colors)):
        if colors[i] == -1:
            if not dfs(i, 0):
                return False

    return True


graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
print(isBipartite(graph))
