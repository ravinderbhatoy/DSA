def peakIndexInMountainArray(arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid-1]:
            return mid
        elif arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [0, 1, 0]
print(peakIndexInMountainArray(arr))
