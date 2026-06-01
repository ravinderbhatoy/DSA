from disjointSet import DisjointSet


def makeConnected(n: int, connections: list[list[int]]) -> int:
    ds = DisjointSet(n)
    extra = 0
    for u, v in connections:
        if ds.find_parent(u) == ds.find_parent(v):
            extra += 1
        else:
            ds.unionBySize(u, v)

    components = 0
    for i in range(n):
        if ds.parent[i] == i:
            components += 1

    ans = components - 1
    return ans if extra >= ans else -1


n = 4
connections = [[0, 1], [0, 2], [1, 2]]

print(makeConnected(n, connections))
