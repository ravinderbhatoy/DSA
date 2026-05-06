def safeNode(graph: list[list[int]]) -> list:
    n = len(graph)
    visited = [False] * n
    path_visited = [False] * n
    isSafe = [False] * n

    def dfsCycle(node):
        visited[node] = True
        path_visited[node] = True

        isSafe[node] = False

        for adj in graph[node]:
            if not visited[adj] and dfsCycle(adj):
                return True  # found a cycle
            elif path_visited[adj]:
                # when a node is visited it has to be on the same path
                return True  # found a cycle

        isSafe[node] = True
        path_visited[node] = False
        return False

    for i in range(n):
        if not visited[i]:
            dfsCycle(i)

    safe_nodes = []

    for i in range(n):
        if isSafe[i]:
            safe_nodes.append(i)

    return safe_nodes


def safeNodesTopoSort(graph: list[list[int]]) -> list:
    from collections import deque

    n = len(graph)
    indegree = [0] * n

    graphRev = [[] for _ in range(n)]

    # reverse the graph
    for i in range(n):
        # before i -> adj
        for adj in graph[i]:
            # after adj -> i
            graphRev[adj].append(i)
            indegree[i] += 1  # indgree of i has been increased

    queue = deque()

    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    res = []
    while queue:
        node = queue.popleft()
        res.append(node)

        for adj in graphRev[node]:
            indegree[adj] -= 1
            if indegree[adj] == 0:
                queue.append(adj)

    res = sorted(res)

    return res


graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
print(safeNodesTopoSort(graph))
