def floydWashall(cost: list[list[int]]):
    n = len(cost)
    # the node using which we are trying to find path

    for i in range(n):
        for j in range(n):
            if cost[i][j] == -1:
                cost[i][j] = int(1e8)

    for via in range(n):
        for i in range(n):
            for j in range(n):
                cost[i][j] = min(cost[i][j], cost[i][via] + cost[via][j])

    return cost


cost = [[0, 4, 1e8, 5, 1e8],
        [1e8, 0, 1, 1e8, 6],
        [2, 1e8, 0, 3, 1e8],
        [1e8, 1e8, 1, 0, 2],
        [1, 1e8, 1e8, 4, 0]]

floydWashall(cost)
print(cost)
