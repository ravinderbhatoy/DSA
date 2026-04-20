def findCircleNum(start, isConnected: list[list[int]]) -> int:
    n = len(isConnected)
    visited = [0] * n
    cnt = 0

    def dfs(node):
        nonlocal isConnected, visited, cnt
        visited[node] = 1

        # Explore all possible neighbors (columns in the isConnected)

        for i in range(n):
            if isConnected[node][i] == 1 and not visited[i]:
                dfs(i)

    for i in range(n):
        if (not visited[i]):
            cnt += 1
            dfs(i)

    return cnt


isConnected = [[1, 1, 0],
               [1, 1, 0],
               [0, 0, 1]]

start = 1

print(findCircleNum(start, isConnected))
