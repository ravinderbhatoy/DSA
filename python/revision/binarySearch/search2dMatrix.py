def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    """
    Start search from top right
    """
    n, m = len(matrix), len(matrix[0])
    row, col = 0, m - 1

    while row < n and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1

    return False


matrix = [[1, 3, 5, 7],
          [10, 11, 16, 20],
          [23, 30, 34, 60]]
target = 3

print(searchMatrix(matrix, target))
