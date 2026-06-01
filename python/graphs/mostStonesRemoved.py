from disjointSet import DisjointSet


def removeStones(stones: list[list[int]]) -> int:
    maxRow, maxCol = 0, 0

    for row, col in stones:
        # in which row and col was last stone placed
        maxRow = max(maxRow, row)
        maxCol = max(maxCol, col)

    ds = DisjointSet(maxRow + maxCol + 1)

    stoneNodes = set()
    for row, col in stones:
        nodeCol = col + maxRow + 1
        ds.unionBySize(row, nodeCol)
        # keeping only nodes that have stones
        stoneNodes.add(row)
        stoneNodes.add(nodeCol)

    cnt = 0
    for node in stoneNodes:
        if ds.find_parent(node) == node:
            cnt += 1  # ultimate parent

    return len(stones) - cnt


stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
print(removeStones(stones))
