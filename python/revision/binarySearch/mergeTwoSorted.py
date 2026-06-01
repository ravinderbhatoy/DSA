def findMedianSorted(nums1, nums2):
    if nums1:
        nums1.extend(nums2)
        nums1 = sorted(nums1)

    if not nums1 and nums2:
        nums1 = nums2

    n = len(nums1)

    if n & 1 == 0:
        mid = n // 2 - 1
        print(mid)
        return (nums1[mid] + nums1[mid + 1]) / 2

    return nums1[n // 2]


nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSorted(nums1, nums2))
