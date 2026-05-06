from collections import deque


def numEnclaves(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[0] * cols for _ in range(rows)]
    queue = deque()

    # 1. Identify all boundary land cells (1s)
    for r in range(rows):
        for c in range(cols):
            # If cell is on the boundary and is land
            if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and grid[r][c] == 1:
                queue.append((r, c))
                visited[r][c] = 1  # MARK IMMEDIATELY

    # 2. Standard BFS to find all land reachable from the boundary
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (0 <= nr < rows and 0 <= nc < cols and
                    not visited[nr][nc] and grid[nr][nc] == 1):
                visited[nr][nc] = 1  # MARK IMMEDIATELY
                queue.append((nr, nc))

    # 3. Count land cells that were NOT visited
    cnt = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and not visited[i][j]:
                cnt += 1

    return cnt


grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
print(numEnclaves(grid))
