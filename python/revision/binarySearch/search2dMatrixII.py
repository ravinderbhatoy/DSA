def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    rs, re = 0, len(matrix) - 1
    isLower = True

    while rs <= re:
        rm = (rs + re) // 2
        cs, ce = 0, len(matrix[0]) - 1

        while cs <= ce:
            cm = (cs + ce) // 2

            if matrix[rm][cm] == target:
                return True
            elif matrix[rm][cm] < target:
                cs = cm + 1
                isLower = True
            else:
                ce = cm - 1
                isLower = False

        if isLower:
            rs = rm + 1
        else:
            re = rm - 1

    return False


matrix = [[1, 4, 7, 11, 15],
          [2, 5, 8, 12, 19],
          [3, 6, 9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]]

target = 5

print(searchMatrix(matrix, target))
