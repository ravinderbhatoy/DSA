def spiralOrder(matrix: list[list[int]]) -> list[int]:
    ans = list()
    top = 0
    right = len(matrix[0]) - 1
    left = 0
    bottom = len(matrix) - 1

    while top <= bottom and left <= right:
        # print top-left -> top- right
        for j in range(left, right + 1):
            ans.append(matrix[top][j])
        top += 1

        # print top-right -> bottom-right
        for i in range(top, bottom + 1):
            ans.append(matrix[i][right])
        right -= 1

        # print bottom-right -> bottom-left
        if top <= bottom:
            for j in range(right, left - 1, -1):
                ans.append(matrix[bottom][j])
            bottom -= 1

        # print bottom-left -> top-left
        if left <= right:
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
        left += 1

    return ans


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(spiralOrder(matrix))
