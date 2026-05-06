from collections import deque


def hasCycle(adj):
    visited = [0] * len(adj)
    path_visited = [0] * len(adj)

    def dfsCheck(node):
        visited[node] = 1
        path_visited[node] = 1

        for nei in adj[node]:
            # when the node is not visited
            if not visited[nei]:
                if dfsCheck(nei):
                    return True
            # when the node is visited
            elif path_visited[nei]:
                # it has to be on the same path
                return True

        path_visited[node] = 0
        return False

    for i in range(len(adj)):
        if not visited[i] and dfsCheck(i):
            return True

    return False


def hasCycleBFS(adj):
    n = len(adj)
    indegree = [0] * n
    queue = deque()
    # res = [] or just use cnt
    cnt = 0

    for i in range(n):
        for nei in adj[i]:
            indegree[nei] += 1

    for i in range(n):
        if indegree == 0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        cnt += 1

        for nei in adj[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)

    return False if cnt == n else True


graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
print(hasCycleBFS(graph))
