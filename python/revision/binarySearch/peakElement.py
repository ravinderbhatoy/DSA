def findPeakElementLessCode(nums):
    s, e = 0, len(nums) - 1

    # Use s < e so that mid + 1 is always a valid index
    while s < e:
        mid = (s + e) // 2

        # If mid is ascending to the right, a peak must be on the right side
        if nums[mid] < nums[mid + 1]:
            s = mid + 1
        # If mid is descending to the right, mid itself could be a peak,
        # or the peak is to the left
        else:
            e = mid

    # When s == e, they will point to a peak element index
    return s


def findPeakElement(nums: list[int]) -> int:
    s, e = 0, len(nums) - 1

    # single element
    if s == e:
        return s

    while s <= e:
        mid = (s + e) // 2

        if mid == 0:
            if nums[mid] > nums[mid + 1]:
                return mid
            else:
                s = mid + 1
        elif mid == len(nums) - 1:
            if nums[mid] > nums[mid - 1]:
                return mid
            else:
                e = mid - 1
        else:
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid - 1] < nums[mid] < nums[mid + 1]:
                s = mid + 1
            else:
                e = mid - 1

    return -1


nums = [1, 2, 4, 2, 0, 3, 7, 9, 6]
print(findPeakElement(nums))
