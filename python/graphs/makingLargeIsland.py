from disjointSet import DisjointSet


def largestIsland(grid: list[list[int]]) -> int:
    N = len(grid)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    ds = DisjointSet(N * N)

    def isValid(r, c):
        return (0 <= r < N and 0 <= c < N
                and grid[r][c] == 1)

    hasZero = False
    # Step: 1 Connect components
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                for dr, dc in directions:
                    nr, nc = dr + i, dc + j
                    if isValid(nr, nc):
                        # formula(getNode) => rowNo. * Cols + colNo.
                        node = i * N + j
                        adjNode = nr * N + nc
                        ds.unionBySize(node, adjNode)
            else:
                hasZero = True

    if not hasZero:
        return N * N

    # Step: 2 Flip water 0 -> 1 and connect
    largest = -1
    for i in range(N):
        for j in range(N):
            unique_components = set()
            if grid[i][j] == 0:
                for dr, dc in directions:
                    nr, nc = dr + i, dc + j
                    if isValid(nr, nc):
                        # formula(getNode) => rowNo. * Cols + colNo.
                        node = nr * N + nc
                        unique_components.add(ds.find_parent(node))

                area = 1 + sum(ds.size[parent] for parent in unique_components)
                largest = max(area, largest)
    return largest


grid = [[1, 1], [1, 0]]
print(largestIsland(grid))
