def isValid(arr: list, c: int, mid: int) -> bool:
    count = 1
    current = 0

    for i in range(1, len(arr)):
        distance = arr[i] - arr[current]
        if distance >= mid:
            count += 1
            current = i
        if count == c:
            return True
    return False


def allocateCows(arr: list, c: int) -> int:
    arr = sorted(arr)
    st = 1
    end = arr[-1] - arr[0]
    ans = -1

    while st <= end:
        mid = st + (end - st) // 2

        if isValid(arr, c, mid):
            print(f"{mid} is valid")
            ans = mid
            st = mid + 1
        else:
            end = mid - 1

    return ans


# log(sum) * O(n)


arr = [2, 24, 16, 32]
print(allocateCows(arr, 3))
