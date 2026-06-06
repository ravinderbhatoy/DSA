def isKSortedArray(arr: list[int], k: int) -> str:
    prevIndexes = {arr[i]: i for i in range(len(arr))}

    arr = sorted(arr)
    targetIndexes = {arr[i]: i for i in range(len(arr))}

    for key in prevIndexes.keys():
        diff = abs(prevIndexes[key] - targetIndexes[key])
        print(diff)
        if diff > k:
            return "No"

    return "Yes"


arr = [13, 8, 10, 7, 15, 14, 12]
k = 1
arr = [3, 2, 1, 5, 6, 4]
k = 2
arr = [18, 44, 12, 27, 4, 19, 42, 8, 34, 15,
       38, 5, 16, 47, 1, 6, 32, 40, 10, 33, 22]

k = 18
print(isKSortedArray(arr, k))
