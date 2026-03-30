def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list:
    e = m + n - 1  # track zero index
    left = m - 1
    right = n - 1

    while left >= 0 and right >= 0:
        if nums1[left] >= nums2[right]:
            nums1[left], nums1[e] = nums1[e], nums1[left]
            left -= 1
            e -= 1
        else:
            nums2[right], nums1[e] = nums1[e], nums2[right]
            right -= 1
            e -= 1

    while right >= 0:
        nums1[e] = nums2[right]
        e -= 1
        right -= 1


nums1 = [4, 5, 6, 0, 0, 0]
nums2 = [1, 2, 3]

merge(nums1, 3, nums2, 3)
print(nums1)
