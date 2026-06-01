def findTheCity(n, edges: list[list[int]], distanceThreshold: int):
    # using Floyd's Warshell

    cost = [[float('inf')] * n for _ in range(n)]
    cities = [0] * n

    # creating cost matrix
    for u, v, w in edges:
        if u != v:
            cost[u][v] = w
            cost[v][u] = w
        else:
            cost[u][v] = 0

    for via in range(n):
        for i in range(n):
            for j in range(n):
                cost[i][j] = min(cost[i][j], cost[i][via] + cost[via][j])

    for i in range(n):
        for j in range(n):
            if i != j:
                # cost of going from city i -> j
                if cost[i][j] <= distanceThreshold:
                    cities[i] += 1

    mini = float('inf')
    city = 0
    for i in range(len(cities)):
        if cities[i] <= mini:
            city = i
            mini = cities[i]

    return city


n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distanceThreshold = 4

print(findTheCity(n, edges, distanceThreshold))
