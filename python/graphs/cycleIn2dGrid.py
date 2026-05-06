def detectCycle(grid: list[list[int]]) -> bool:
    rows = len(grid)
    cols = len(grid[0])
    visited = [[0] * cols for _ in range(rows)]

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(r, c, pr, pc):
        visited[r][c] = 1
        for dr, dc in directions:
            nr, nc = dr + r, dc + c
            # we found a matching cell
            if (0 <= nr < rows and 0 <= nc < cols and
                    grid[nr][nc] == grid[r][c]):
                if visited[nr][nc]:
                    # 2. If the neighbor is visited and it's NOT
                    # the parent we just came from
                    if (nr, nc) != (pr, pc):
                        return True  # cycle detected
                else:
                    if dfs(nr, nc, r, c):
                        return True

        return False

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j] and dfs(i, j, -1, -1):
                return True

    return False


grid = [["a", "b", "b"],
        ["b", "z", "b"],
        ["b", "b", "a"]]
print(detectCycle(grid))
