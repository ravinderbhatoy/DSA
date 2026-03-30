def ratInMaze(maze):
    res = []
    n = len(maze)
    visited = [[0] * n for i in range(n)]

    if not maze[0][0] or not maze[n-1][n-1]:
        return res

    dirs = "DLRU"
    # direction of i (down / up)
    di = [+1, 0, 0, -1]
    # direction of j (left / right)
    dj = [0, -1, 1, 0]

    # striver method
    def getPath(i, j, path):
        if i == n-1 and j == n-1:
            res.append(path)
            return

        for ind in range(0, 4):  # 4 directions
            nexti = i + di[ind]
            nextj = j + dj[ind]
            if (nexti >= 0 and nextj >= 0 and nexti < n and nextj < n
                    and not visited[nexti][nextj] and maze[nexti][nextj] == 1):

                visited[i][j] = 1
                getPath(nexti, nextj, path + dirs[ind])
                visited[i][j] = 0

    def backtrack(row, col, path):
        # apna college method
        if row < 0 or col < 0 or row >= n or col >= n:
            # out of boundary
            return

        if maze[row][col] != 1:
            return

        if row == n-1 and col == n-1:
            # path found
            res.append(path)
            return

        maze[row][col] = -1

        backtrack(row+1, col, path + 'D')  # down
        backtrack(row, col - 1, path + 'L')  # left
        backtrack(row, col + 1, path + 'R')  # right
        backtrack(row-1, col, path + 'U')  # up

        maze[row][col] = 1

    # backtrack(0, 0, "")
    getPath(0, 0, "")
    return res


maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]]

print(ratInMaze(maze))
