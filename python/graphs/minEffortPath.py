import heapq


def minimumEffortPath(heights: list[list[int]]) -> int:
    rows, cols = len(heights), len(heights[0])
    sr, sc = 0, 0
    tr, tc = rows - 1, cols - 1

    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[sr][sc] = 0

    # (weight, row, col)
    pq = [(0, 0, 0)]

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while pq:
        diff, r, c = heapq.heappop(pq)

        if r == tr and c == tc:
            return diff

        for dr, dc in directions:
            nr, nc = dr + r, dc + c

            # checking valid movement
            if 0 <= nr < rows and 0 <= nc < cols:
                # cal abs effort and track max
                new_effort = max(abs(heights[r][c] - heights[nr][nc]), diff)
                if new_effort < dist[nr][nc]:
                    dist[nr][nc] = new_effort
                    heapq.heappush(pq, (new_effort, nr, nc))
    return 0


heights = [[1, 2, 2],
           [3, 8, 2],
           [5, 3, 5]]
print(minimumEffortPath(heights))
