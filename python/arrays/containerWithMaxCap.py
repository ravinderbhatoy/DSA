def maxCapacity(heights):
    maxCap = 0
    for i in range(0, len(heights)):
        capacity = 0
        for j in range(i + 1, len(heights)):
            area = j - i
            capacity = min(heights[j], heights[i]) * area
            maxCap = max(capacity, maxCap)
    return maxCap


# optimal solution
def maxArea(heights):
    maxCap = 0
    left = 0
    right = len(heights) - 1

    while left < right:
        minHeight = min(heights[left], heights[right])
        width = right - left
        capacity = width * minHeight
        maxCap = max(maxCap, capacity)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return maxCap


print(maxCapacity([1, 2]))
print(maxArea([1, 2]))
