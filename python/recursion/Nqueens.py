def Nqueen(n: int):
    board = [['.'] * n for i in range(n)]  # stores board state
    ans = []  # to return all possible states

    rowHash = [0] * n
    lowerDiagonalHash = [0] * (2 * n - 1)
    upperDiagonalHash = [0] * (2 * n - 1)

    def solve(col, board, ans, n):
        if (col == n):
            ans.append([''.join(row) for row in board])
            return

        for row in range(0, n):
            if (rowHash[row] == 0 and lowerDiagonalHash[row + col] == 0
                    and upperDiagonalHash[(n - 1) + col - row] == 0):
                board[row][col] = 'Q'
                # update hash
                rowHash[row] = 1
                lowerDiagonalHash[row + col] = 1
                upperDiagonalHash[(n - 1) + col - row] = 1
                solve(col + 1, board, ans, n)
                board[row][col] = '.'
                # toggle hash
                rowHash[row] = 0
                lowerDiagonalHash[row + col] = 0
                upperDiagonalHash[(n - 1) + col - row] = 0
    solve(0, board, ans, n, ans)
    return ans


ans = Nqueen(4)
for board in ans:
    print(board)

# --------------- Brute force safe check -----------------------

# def isSafe(row, col, board, n):
#         # vertical check
#         duprow = row
#         dupcol = col
#
#         # horizontal check
#         while col >= 0:
#             if board[row][col] == 'Q':
#                 return False
#             col -= 1
#
#         # upper left diagonal check
#         col = dupcol
#         while row >= 0 and col >= 0:
#             if board[row][col] == 'Q':
#                 return False
#             row -= 1
#             col -= 1
#
#         # lower left diagonal check
#         row = duprow
#         col = dupcol
#         while (row < n and col >= 0):
#             if board[row][col] == 'Q':
#                 return False
#             row += 1
#             col -= 1
#
#         # no attacking
#         return True
