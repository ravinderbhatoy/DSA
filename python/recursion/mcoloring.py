def graphColoring(v, edges, m):
    # build adjacency list
    adj = [[] for _ in range(v)]
    for u, w in edges:
        adj[u].append(w)
        adj[w].append(u)

    colors = [0] * v

    def isSafe(node, color):
        for nei in adj[node]:
            if colors[nei] == color:
                return False
        return True

    def solve(node):
        if node == v:
            return True

        for col in range(1, m + 1):
            if isSafe(node, col):
                colors[node] = col
                if solve(node + 1):
                    return True
                colors[node] = 0

        return False

    return solve(0)


V = 4
edges = [[0, 1], [1, 2], [2, 3], [0, 3]]
m = 2


print(graphColoring(V, edges, m))
