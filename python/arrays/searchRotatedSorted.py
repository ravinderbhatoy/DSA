def search(nums: list[int], target: int) -> int:
    st = 0
    end = len(nums) - 1

    while st <= end:
        mid = (st + end) // 2

        if nums[mid] == target:
            return mid

        if nums[st] <= nums[mid]:
            # left part is sorted
            if nums[st] <= target and target <= nums[mid]:
                end = mid - 1
            else:
                st = mid + 1
        else:
            # right part is sorted
            if nums[mid] <= target and target <= nums[end]:
                st = mid + 1
            else:
                end = mid - 1
    return -1


nums = [3, 4, 5, 6, 7, 0, 1, 2]
target = 3

print(search(nums, target))
