from disjointSet import DisjointSet


def numOfIslands(rows: int, cols: int,
                 operators: list[list[int]]) -> list[int]:
    ds = DisjointSet(rows * cols)
    visited = [[0] * cols for _ in range(rows)]

    def isValid(row, col):
        return 0 <= row < rows and 0 <= col < cols

    ans = []
    cnt = 0  # no. of islands
    # right,  bottom  left top
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for row, col in operators:
        if visited[row][col]:
            ans.append(cnt)
            continue

        visited[row][col] = 1
        cnt += 1

        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if (isValid(nr, nc) and visited[nr][nc]):
                # checking connection
                nodeNo = row * cols + col
                adjNode = nr * cols + nc

                if ds.find_parent(nodeNo) != ds.find_parent(adjNode):
                    cnt -= 1
                    ds.unionBySize(nodeNo, adjNode)

        ans.append(cnt)

    return ans


n = 4
m = 5
k = 4
A = [[1, 1], [0, 1], [3, 3], [3, 4]]

print(numOfIslands(n, m, A))
