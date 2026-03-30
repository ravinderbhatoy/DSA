def merge(arr, low, mid, high):
    left = low
    right = mid + 1
    temp = list()

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    # place elements into actual array
    for i in range(low, high + 1):
        arr[i] = temp[i - low]


def mergeSort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)
    merge(arr, low, mid, high)


arr = [3, 5, 2, 1, 4]
mergeSort(arr, 0, len(arr) - 1)
print(arr)
