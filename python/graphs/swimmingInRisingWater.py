import heapq


def swimWater(grid: list[list[int]]) -> int:
    N = len(grid)

    pq = [(grid[0][0], 0, 0)]  # time, x, y
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    visited = [[False] * N for _ in range(N)]
    visited[0][0] = True

    while pq:
        elevation, r, c = heapq.heappop(pq)
        if r == N - 1 and c == N-1:
            return elevation

        for dr, dc in directions:
            nr, nc = dr + r, dc + c

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = True
                heapq.heappush(pq, (max(elevation, grid[nr][nc]), nr, nc))

    return -1


grid = [[0, 1, 2, 3, 4],
        [24, 23, 22, 21, 5],
        [12, 13, 14, 15, 16],
        [11, 17, 18, 19, 20],
        [10, 9, 8, 7, 6]]

print(swimWater(grid))
