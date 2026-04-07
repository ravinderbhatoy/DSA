def subsequences(arr: list[int], ind: int, sub: list[int]):
    """
    print all subsequences
    """
    if ind >= len(arr):
        print(sub)
        return
    # pick element at a particular index to add in subsequence
    sub.append(arr[ind])
    subsequences(arr, ind + 1, sub)
    # remove element at a particular index to exclude from subsequence
    sub.pop()
    subsequences(arr, ind + 1, sub)


def subsequenceWithSumK(arr: list[int], sub: list[int], ind: int, k: int, sum: int):
    """
    print all subsequences with sum k
    """
    if ind >= len(arr):
        if sum == k:
            print(sub)
        return
    sum += arr[ind]
    sub.append(arr[ind])
    subsequenceWithSumK(arr, sub, ind + 1, k, sum)
    sum -= arr[ind]
    sub.pop(-1)
    subsequenceWithSumK(arr, sub, ind + 1, k, sum)


def onlyOneSubsequenceWithSumK(arr: list[int], sub: list[int], ind: int, k: int, sum: int):
    """
    print one subsequences with sum k
    """
    if ind == len(arr):
        if sum == k:
            print(sub)
            return True
        else:
            return False
    sum += arr[ind]
    sub.append(arr[ind])
    if onlyOneSubsequenceWithSumK(arr, sub, ind + 1, k, sum) is True:
        return True
    sum -= arr[ind]
    sub.pop()
    if onlyOneSubsequenceWithSumK(arr, sub, ind + 1, k, sum) is True:
        return True
    return False


def countSubsequencesWithSumK(arr: list[int], ind: int, k: int, sum: int,
                              count: int):
    # if only positive integers return is sum exceeds k
    if sum > k:
        return 0
    if ind >= len(arr):
        if sum == k:
            return 1
        return 0
    sum += arr[ind]
    left = countSubsequencesWithSumK(arr, ind + 1, k, sum, count)
    sum -= arr[ind]
    right = countSubsequencesWithSumK(arr, ind + 1, k, sum, count)
    return left + right


arr1 = [3, 1, 2]
arr2 = [1, 2, 1]
subsequences(arr1, 0, [])
# onlyOneSubsequenceWithSumK(arr2, [], 0, 2, 0)
# print(countSubsequencesWithSumK(arr2, 0, 2, 0, 0))
