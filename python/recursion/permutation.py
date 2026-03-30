def getPermutation(arr: [int], ind):
    if ind >= len(arr):
        print(arr)
        return
    for i in range(ind, len(arr)):
        arr[i], arr[ind] = arr[ind], arr[i]
        getPermutation(arr, ind + 1)
        arr[i], arr[ind] = arr[ind], arr[i]


arr = [1, 2, 3]
getPermutation(arr, 0)
