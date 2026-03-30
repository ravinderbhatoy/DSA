def trap(height):
    # if len(height) < 3:
    #     return 0
    # lmax = height[0]
    # capacity = 0
    # for i in range(1, len(height)-1):
    #     rmax = height[i]
    #     # find the right max
    #     for j in range(i+1, len(height)):
    #         rmax = max(rmax, height[j])
    #     if height[i] < lmax and height[i] < rmax:
    #         capacity += min(lmax, rmax) - height[i]
    #     lmax = max(lmax, height[i])
    # return capacity
    left, right = 0, len(height) - 1
    lmax = rmax = 0
    water = 0

    while left < right:
        lmax = max(lmax, height[left])
        rmax = max(rmax, height[right])

        if lmax < rmax:
            water += lmax - height[left]
            left += 1
        else:
            water += rmax - height[right]
            right -= 1
    return water


def trapWater(height):
    size = len(height)
    lmax = [0] * size
    rmax = [0] * size
    lmax[0] = height[0]
    rmax[size - 1] = height[size - 1]

    for i in range(1, size):
        lmax[i] = max(lmax[i-1], height[i])

    for i in range(size-2, -1, -1):
        rmax[i] = max(rmax[i+1], height[i])

    water = 0
    for i in range(size):
        water += min(lmax[i], rmax[i]) - height[i]

    return water


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [5, 4, 1, 2]
print(trap(height))
print(trapWater(height))
