def reverseRec(data, low, high):
    if low >= high:
        return
    data[low], data[high] = data[high], data[low]
    reverseRec(data, low + 1, high - 1)


arr = [1, 2, 3, 4, 5]
reverseRec(arr, 0, len(arr) - 1)
print(arr)
