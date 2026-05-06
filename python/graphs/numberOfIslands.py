def numberOfIslands(grid: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    visited = [[0] * cols for _ in range(rows)]
    islands = 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(r, c):
        visited[r][c] = 1
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                    grid[nr][nc] == "1" and not visited[nr][nc]):
                dfs(nr, nc)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1" and not visited[i][j]:
                dfs(i, j)
                islands += 1

    return islands


grids = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(numberOfIslands(grids))
