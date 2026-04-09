def largestRectangleArea(heights: list[int]) -> int:
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
