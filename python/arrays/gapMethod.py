import math


class Solution:
    def swapIfGreater(self, nums1: list[int], nums2: list[int], left, right):
        if nums1[left] > nums2[right]:
            nums1[left], nums2[right] = nums2[right], nums1[left]

    def merge(self, nums1: list[int], nums2: list[int], n: int, m: int):
        size = n + m
        gap = math.ceil(size / 2)  # this will give ceil value for odd numbers
        while gap > 0:
            left = 0
            right = left + gap
            while right < size:
                if left < n and right >= n:
                    # nums1 and nums2
                    self.swapIfGreater(nums1, nums2, left, right - n)
                elif left >= n:
                    # nums2 and nums2
                    self.swapIfGreater(nums2, nums2, left - n, right - n)
                else:
                    # nums1 and nums1
                    self.swapIfGreater(nums1, nums1, left, right)
                left += 1
                right += 1
            if gap == 1:
                break
            else:
                gap = math.ceil(gap / 2)

    def merge2(self, nums1: list[int], nums2: list[int], n: int, m: int):
        left = n - 1
        right = 0

        while left >= 0 and right < m:
            if nums1[left] > nums2[right]:
                nums1[left], nums2[right] = nums2[right], nums1[left]
                left -= 1
                right += 1
            else:
                break

        nums1[:] = sorted(nums1)
        nums2[:] = sorted(nums2)


s = Solution()
nums1 = [1, 3, 5, 7]
nums2 = [0, 2, 6, 8, 9]

s.merge2(nums1, nums2, len(nums1), len(nums2))
print(nums1)
print(nums2)
