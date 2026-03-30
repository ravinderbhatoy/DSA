def union(nums1: list[int], nums2: list[int]) -> list[int]:
    temp = []
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            if not temp or temp[-1] != nums1[i]:
                temp.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] > nums2[j]:
            if not temp or temp[-1] != nums2[j]:
                temp.append(nums2[j])
            j += 1
        else:
            if not temp or temp[-1] != nums1[i]:
                temp.append(nums1[i])
            i += 1

    while i < len(nums1):
        if not temp or temp[-1] != nums1[i]:
            temp.append(nums1[i])
        i += 1

    while j < len(nums2):
        if not temp or temp[-1] != nums2[j]:
            temp.append(nums2[j])
        j += 1

    return temp


# merge will also have duplicates unlike union
def merge(nums1: list[int], m: int, nums2: list[int], n: int):
    # m -> non zero elements in nums1
    i, j = m - 1, n - 1
    idx = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[idx] = nums1[i]
            i -= 1
        elif nums1[i] < nums2[j]:
            nums1[idx] = nums2[j]
            j -= 1
        else:
            nums1[idx] = nums1[i]
            i -= 1
        idx -= 1

    while j >= 0 and idx >= 0:
        nums1[idx] = nums2[j]
        j -= 1
        idx -= 1

    return nums1


nums1 = [1, 2, 3]
nums2 = [2, 3, 4]
print(union(nums1, nums2))
# print(merge(nums1, 3, nums2, 3))
