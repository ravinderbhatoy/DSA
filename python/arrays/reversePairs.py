cnt = 0


def merge(nums, low, mid, high):
    left = low
    right = mid + 1
    temp = list()
    global cnt

    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1

    while left <= mid:
        temp.append(nums[left])
        left += 1

    while right <= high:
        temp.append(nums[right])
        right += 1

    for i in range(low, high + 1):
        nums[i] = temp[i - low]

    return cnt


def countPairs(nums, low, mid, high):
    global cnt
    right = mid + 1
    for i in range(low, mid + 1):
        while right <= high and nums[i] > (2 * nums[right]):
            right += 1
        cnt += right - (mid + 1)


def mergeSort(nums, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    mergeSort(nums, low, mid)
    mergeSort(nums, mid + 1, high)
    countPairs(nums, low, mid, high)
    merge(nums, low, mid, high)


def reversePairs(nums):
    mergeSort(nums, 0, len(nums) - 1)
    return cnt


nums = [2, 4, 3, 5, 1]
print(reversePairs(nums))
