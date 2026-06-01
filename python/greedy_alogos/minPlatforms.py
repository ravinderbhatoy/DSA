def minPlatform(arr: list[int], dep: list[int]) -> int:
    maxCount = 0
    cnt = 0

    arr = sorted(arr)
    dep = sorted(dep)
    i = j = 0

    while i < len(arr):
        if arr[i] < dep[j]:
            i += 1
            cnt += 1
        else:
            j += 1
            cnt -= 1

        maxCount = max(cnt, maxCount)

    return maxCount


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

print(minPlatform(arr, dep))
