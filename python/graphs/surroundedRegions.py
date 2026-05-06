def surrounded_regions(board: list[list[int]]) -> None:
    """Modify input"""

    rows = len(board)
    cols = len(board[0])
    visited = [[0] * cols for _ in range(rows)]

    def dfs(r, c):
        visited[r][c] = 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (0 <= nr < rows and 0 <= nc < cols and
                    not visited[nr][nc] and board[nr][nc] == 'O'):
                dfs(nr, nc)

    # Traverse all boundaries

    # Travers firt and last row
    for j in range(cols):
        # first row
        if not visited[0][j] and board[0][j] == 'O':
            dfs(0, j)
        # last row
        if not visited[rows-1][j] and board[rows-1][j] == 'O':
            dfs(rows-1, j)

    # Traverse top and bottom row
    for i in range(rows):
        # top row
        if not visited[i][0] and board[i][0] == 'O':
            dfs(i, 0)
        # bottom row
        if not visited[i][cols-1] and board[i][cols-1] == 'O':
            dfs(i, cols - 1)

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                board[i][j] = 'X'


board = [["X", "X", "X", "X"],
         ["X", "O", "O", "X"],
         ["X", "X", "O", "X"],
         ["X", "O", "X", "X"]]

# board = [["O", "O"], ["O", "O"]]

surrounded_regions(board)
print(board)
