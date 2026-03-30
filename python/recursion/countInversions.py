def inversionCount(arr):
    def merge(arr, low, mid, high):
        left = low
        right = mid + 1
        temp = list()
        count = 0

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
                count += mid - left + 1

        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp[i - low]
        return count

    def mergeSort(arr, low, high):
        if low >= high:
            return 0
        mid = (low + high) // 2
        leftCount = mergeSort(arr, low, mid)
        rightCount = mergeSort(arr, mid + 1, high)
        count = merge(arr, low, mid, high)
        return leftCount + rightCount + count

    return mergeSort(arr, 0, len(arr) - 1)


arr = [2, 3, 7, 1, 3, 0]
print(inversionCount(arr))
