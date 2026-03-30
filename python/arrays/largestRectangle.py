def largestRectangleArea(heights: [int]) -> int:
    maxiArea = 0
    for i in range(len(heights)):
        minHeight = heights[i]
        for j in range(i, len(heights)):
            minHeight = min(minHeight, heights[j])
            width = j - i + 1
            maxiArea = max(maxiArea, minHeight * width)
    return maxiArea


def findPse(nums):
    # find left smallest values
    pse = [0] * len(nums)
    stack = list()

    for i in range(len(heights)):
        while len(stack) and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if len(stack):
            pse[i] = stack[-1]
        else:
            pse[i] = -1
        stack.append(i)

    return pse


def findNse(nums):
    # find right smallest values
    nse = [0] * len(nums)
    stack = list()

    for i in range(len(heights) - 1, -1, -1):
        while len(stack) and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if len(stack):
            nse[i] = stack[-1]
        else:
            nse[i] = len(heights)
        stack.append(i)

    return nse


def optimal(heights) -> int:
    nse = findNse(heights)
    pse = findPse(heights)

    maxArea = 0

    for i in range(len(heights)):
        maxArea = max(maxArea, heights[i] * (nse[i] - pse[i] - 1))

    return maxArea


def moreOptimal(heights):
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

    print(maxArea)
    while len(stack):
        nse = len(heights)
        top = stack.pop()
        pse = stack[-1] if len(stack) else -1
        maxArea = max(heights[top] * (nse-pse-1), maxArea)

    return maxArea


heights = [2, 1, 5, 6, 2, 3]
print(moreOptimal(heights))
