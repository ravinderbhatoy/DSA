from collections import deque


def topologicalSort(V, adj):
    stack = list()
    visited = [0] * V

    def dfs(node):
        visited[node] = 1

        for nei in adj[node]:
            if not visited[nei]:
                dfs(nei)

        stack.append(node)

    for i in range(V):
        if not visited[i]:
            dfs(i)

    return stack[::-1]


def kahnsAlogrithm(V, adj):
    # using BFS
    in_degress = [0] * V  # no. of incoming edges
    res = []
    queue = deque()

    for i in range(V):
        for nei in adj[i]:
            in_degress[nei] += 1

    for i in range(V):
        if in_degress[i] == 0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        res.append(node)

        for nei in adj[node]:
            in_degress[nei] -= 1
            if in_degress[nei] == 0:
                queue.append(nei)

    return res
