def maxArea(heights: list[int]) -> int:
    maxi = -1
    area = 1
    i = 0
    j = len(heights) - 1

    while i < j:
        width = j - i
        height = min(heights[j], heights[i])
        area = width * height
        maxi = max(maxi, area)
        if heights[i] < heights[j]:
            i += 1
        else:
            j -= 1
    return maxi


heights = [1, 6, 4, 6, 9, 3, 1]
print(maxArea(heights))
