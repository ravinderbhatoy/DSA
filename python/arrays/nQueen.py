def isSafe(board: list[str], row: int, col: int, n: int):
    # checks row (horizontal)
    for j in range(0, n):
        if board[row][j] == "Q":
            return False

    # checks column (vertical)
    for i in range(0, n):
        if board[i][col] == "Q":
            return False

    # left diagonal check (upper left)
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # right diagnal check (upper right)
    i = row
    j = col
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def nQueen(board: list[str], row: int, n: int, ans):
    if row >= n:
        # ans will contain all possible solutions
        ans.append(board.copy())
        return

    for j in range(0, n):
        if isSafe(board, row, j, n):
            # board[i][j] = "Q"
            board[row] = board[row][:j] + "Q" + board[row][j + 1 :]
            nQueen(board, row + 1, n, ans)
            board[row] = board[row][:j] + "." + board[row][j + 1 :]
            # board[i][j] = "."


n = 4
board = []
for i in range(n):
    row = ""
    for j in range(n):
        row += "."
    board.append(row)

ans = []
nQueen(board, 0, n, ans)


print(ans)
