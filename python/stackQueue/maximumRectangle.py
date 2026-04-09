def maximumRectangle(matrix: list[list[int]]) -> int:
    def largestRectangleArea(heights):
        maxArea = 0
        stack = list()
        for i in range(len(heights)):
            # area[i] = area[i] * nse - pse - 1
            while len(stack) and heights[stack[-1]] >= heights[i]:
                # calculate area for stack top
                top = stack.pop()
                nse = i
                pse = stack[-1] if len(stack) else -1
                maxArea = max(heights[top] * (nse - pse - 1), maxArea)
            stack.append(i)

        while len(stack):
            nse = len(heights)
            top = stack.pop()
            pse = stack[-1] if len(stack) else -1
            maxArea = max(heights[top] * (nse-pse-1), maxArea)

        return maxArea

    n = len(matrix)
    m = len(matrix[0])

    heights = [0] * m
    maxArea = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "1":
                heights[j] += 1
            else:
                heights[j] = 0
        maxArea = max(largestRectangleArea(heights), maxArea)
    return maxArea


matrix = [["1", "0", "1", "0", "0"],
          ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["1", "0", "1", "1", "1"]]

print(maximumRectangle(matrix))
