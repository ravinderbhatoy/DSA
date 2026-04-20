from collections import deque


def detectCycle(start, visited, adjList) -> bool:
    visited[start] = 1

    queue = deque()
    # (node, parent) parent -> through which node was traversed
    queue.append((start, -1))

    while queue:
        node, parent = queue.popleft()
        for adjNode in adjList[node]:
            if (not visited[adjNode]):
                visited[adjNode] = 1
                queue.append((adjNode, node))
            elif parent != adjNode:
                return True

    return False


def hasCycle(adjList):
    n = len(adjList)
    visited = [0] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i] and detectCycle(i, visited, adjList):
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
