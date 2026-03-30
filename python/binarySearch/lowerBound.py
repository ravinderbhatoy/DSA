def lowerBound(arr: [int], n: int, x: int) -> int:
    """
    Smallest largest element in array than x
    if all elements are smaller return n
    [1,2,2,3], x=0 ans = 1
    """
    low = 0
    high = n - 1
    smInd = -1

    while (low <= high):
        mid = low + (high - low) // 2

        if arr[mid] < x:
            low = mid + 1
        else:
            smInd = mid
            high = mid - 1

    if smInd != -1:
        return smInd
    return n


arr = [1, 2, 2, 3]
x = 0

print(lowerBound(arr, len(arr), x))
