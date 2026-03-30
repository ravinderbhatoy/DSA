def bubbleSort(arr: list) -> list:
    for i in range(0, len(arr)):
        isSwap = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                isSwap = True
        # if not swap is performed means array is already sorted
        if not isSwap:
            return arr

    return arr


def selectionSort(arr: list) -> list:
    for i in range(0, len(arr)):
        mini = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]

    return arr


def insertionSort(arr: list) -> list:
    for i in range(1, len(arr)):
        current = arr[i]
        prev = i - 1
        while arr[prev] > current and prev >= 0:
            arr[prev + 1] = arr[prev]
            print(arr)
            prev -= 1

        arr[prev + 1] = current

    return arr


arr = [5, 2, 6, 7, 8]

print(insertionSort(arr))
