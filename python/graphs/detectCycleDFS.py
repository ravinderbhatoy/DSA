def hasCycle(adjList):
    n = len(adjList)
    visited = [0] * (n + 1)

    def dfs(node, parent):
        visited[node] = 1

        for adj in adjList[node]:
            if not visited[adj]:
                if dfs(adj, node):
                    return True

            elif (adj != parent):
                return True

        return False

    # incase of multiple components

    for i in range(1, n + 1):
        if not visited[i]:
            if dfs(i, -1):
                return True

    return False


adjList = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 4, 6],
    4: [3],
    5: [2, 7],
    6: [3, 7],
    7: [5, 6]
}


print(hasCycle(adjList))
