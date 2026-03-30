def solveSudoku(board):
    def isValid(row, col, c: str):
        for i in range(0, 9):
            if board[i][col] == c:
                return False

            if board[row][i] == c:
                return False

            # to check if number exist in 3x3 grid
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
                return False
        return True

    def solve():
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for c in range(1, 10):
                        if isValid(i, j, str(c)):
                            board[i][j] = str(c)
                            # check if our filling is valid
                            if (solve() is True):
                                return True
                            else:
                                # if not undo
                                board[i][j] = '.'
                    return False
        # no empty cell return true
        return True

    solve()
    return board


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(solveSudoku(board))
