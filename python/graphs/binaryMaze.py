from collections import deque


def shortestpathBinaryMatrix(grid: list[list[int]]) -> int:
    if grid[0][0] == 1:
        return -1

    rows, cols = len(grid), len(grid[0])
    # source row, col
    sr, sc = 0, 0
    # target row, col
    tr, tc = rows - 1, cols - 1

    if tr == sr and tc == sc:
        return 1

    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[sr][sc] = 0

    w = 1  # initial weight
    queue = deque([(sr, sc, w)])  # (row, col, weight)

    # movements
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (-1, 1), (-1, -1), (1, 1), (1, -1)]
    while queue:
        r, c, w = queue.popleft()
        w += 1
        for dr, dc in directions:
            print(queue)
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols
                    and dist[nr][nc] > w and grid[nr][nc] == 0):
                if nr == tr and nc == tc:
                    return w
                dist[nr][nc] = w
                queue.append((nr, nc, w))
    return -1


grid = [[0, 1, 1], [1, 1, 1], [1, 1, 0]]
print(shortestpathBinaryMatrix(grid))
