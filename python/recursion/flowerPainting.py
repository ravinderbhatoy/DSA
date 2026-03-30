def gardenNoAdj(n, paths):
    adj = [[] for _ in range(n + 1)]
    # n -> no. of gardens
    for u, w in paths:
        adj[u].append(w)
        adj[w].append(u)

    flowers = [0] * (n + 1)

    def isSafe(node, color):
        for nei in adj[node]:
            if flowers[nei] == color:
                return False
        return True

    def solve(node):
        if node > n:
            return True

        for col in range(1, 5):
            if isSafe(node, col):
                flowers[node] = col
                print(flowers)
                if solve(node + 1):
                    return True
                flowers[node] = 0
        return False

    solve(1)
    return flowers[1:]


n = 3
paths = [[1, 2], [2, 3], [3, 1]]
print(gardenNoAdj(n, paths))
