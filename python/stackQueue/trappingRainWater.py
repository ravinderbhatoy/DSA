def trapWater(height):
    # calculate prefix sum
    n = len(height)

    left = 0
    right = n - 1

    lmax = height[left]
    rmax = height[right]

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


height = [4, 2, 0, 3, 2, 5]
print(trapWater(height))
