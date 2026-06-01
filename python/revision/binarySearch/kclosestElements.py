def findClosestElement(arr: list[int], k: int, x: int):
    res = []
    left, right = 0, len(arr) - 1

    # found upper bound
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            # we found the actual number
            left = mid
            right = mid - 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    # found lower bound
    left, right = right, left

    print(arr[left], arr[right])

    while len(res) < k and left >= 0 and right < len(arr):
        if abs(arr[left] - x) <= abs(arr[right] - x):
            res.append(arr[left])
            left -= 1
        else:
            res.append(arr[right])
            right += 1

    while len(res) < k and left >= 0:
        res.append(arr[left])
        left -= 1
    while len(res) < k and right < len(arr):
        res.append(arr[right])
        right += 1

    return sorted(res)


arr = [1, 2, 3, 4, 5, 6, 7, 11, 15, 18, 22]
k = 3
x = 6
print(findClosestElement(arr, k, x))
