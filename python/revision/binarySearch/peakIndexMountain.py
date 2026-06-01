def peakIndexInMountainArray(arr: list[int]) -> int:
    s, e = 0, len(arr) - 1

    while s <= e:
        mid = (s + e) // 2

        if arr[mid+1] < arr[mid] > arr[mid-1]:
            return mid
        elif arr[mid] > arr[mid - 1]:
            s = mid + 1
        else:
            e = mid - 1

    return -1


arr = [0, 2, 1, 0]
print(peakIndexInMountainArray(arr))
