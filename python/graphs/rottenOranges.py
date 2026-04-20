from collections import deque


def orangesRotting(grid: list[list[int]]) -> int:

    rows, cols = len(grid), len(grid[0])

    frest_count = 0  # for later comparision
    minutes = 0
    queue = deque()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:  # rotten orange
                queue.append((r, c, minutes))  # (row, col, current_time)
            elif grid[r][c] == 1:
                frest_count += 1

    # there are no fresh oranges to begin with
    if frest_count == 0:
        return 0

    # up     down    right   left
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while queue:
        r, c, time = queue.popleft()
        minutes = time

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                frest_count -= 1

                queue.append((nr, nc, time + 1))

    return minutes if frest_count == 0 else -1
