def findMin(nums: list[int]) -> int:
    s, e = 0, len(nums) - 1
    mini = float('inf')

    while s <= e:
        mid = (s + e) // 2

        if nums[s] <= nums[mid] <= nums[e]:
            e = mid - 1
        else:
            if nums[s] > nums[mid]:
                e = mid - 1
            else:
                s = mid + 1
        mini = min(mini, nums[mid])
    return mini


nums = [3, 4, 5, 1, 2]
nums = [11, 13, 15, 17]
print(findMin(nums))
