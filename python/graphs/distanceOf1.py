from collections import deque


def updateMatrix(mat: list[list[int]]) -> list[list[int]]:
    rows = len(mat)
    cols = len(mat[0])

    # SC (n x m)
    visited = [[0] * cols for _ in range(rows)]
    # SC (n x m)
    queue = deque()  # (row, col, step)
    step = 0

    # TC (n x m)
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                visited[i][j] = 1
                queue.append((i, j, step))

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # SC (n x m)
    distance = [[0] * cols for _ in range(rows)]

    # TC (n x m)
    while queue:
        row, col, step = queue.popleft()
        distance[row][col] = step

        # x4
        for dr, dc in directions:
            nr, nc = row + dr, col + dc

            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                visited[nr][nc] = 1
                queue.append((nr, nc, step + 1))

    return distance


mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
print(updateMatrix(mat))
