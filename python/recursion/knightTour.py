# def checkValidGrid(grid) -> bool:
#     n = len(grid)
#     # false start
#     if grid[0][0] != 0:
#         return False
#
#     pos = {}
#     for r in range(n):
#         for c in range(n):
#             pos[grid[r][c]] = (r, c)
#
#     for step in range(n*n-1):
#         r1, c1 = pos[step]
#         r2, c2 = pos[step+1]
#
#         dr = abs(r1 - r2)
#         dc = abs(c1 - c2)
#
#         if not (dr == 2 and dc == 1 or dc == 2 and dr == 1):
#             return False
#     return True

def checkValidGrid(grid) -> bool:
    n = len(grid)

    def backtrack(r, c, step):
        if r < 0 or r >= n or c < 0 or c >= n or step != grid[r][c]:
            return False

        # last step has been reached
        if step == n*n-1:
            return True

        moves = [
            (2, 1), (2, -1), (-2, 1), (-2, 1),
            (1, -2), (1, 2), (-1, -2), (-1, 2)
        ]

        for dr, dc in moves:
            if backtrack(r + dr, c + dc, step + 1):
                return True
        return False
    return backtrack(0, 0, 0)


grid = [[0, 11, 16, 5, 20],
        [17, 4, 19, 10, 15],
        [12, 1, 8, 21, 6],
        [3, 18, 23, 14, 9],
        [24, 13, 2, 7, 22]]

print(checkValidGrid(grid))
