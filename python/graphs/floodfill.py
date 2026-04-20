from collections import deque


def floodfill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    rows, cols = len(image), len(image[0])
    queue = deque()

    start_color = image[sr][sc]
    queue.append((sr, sc))  # (row, col, color)

    # vertical and horizontal movements
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = dr + r, dc + c
            if (0 <= nr < rows and 0 <= nc < cols and
                    image[nr][nc] == start_color and image[nr][nc] != color):
                queue.append((nr, nc))
                image[nr][nc] = color

    return image


image = [[0, 0, 0], [0, 0, 0]]
sr = 0
sc = 0
color = 0
print(floodfill(image, sr, sc, color))
