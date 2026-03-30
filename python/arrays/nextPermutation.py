def nextPermutation(nums: list[int]):
    # find the pivot element
    pivot = -1

    for i in range(len(nums) - 1, 0, -1):
        if nums[i - 1] < nums[i]:
            pivot = i - 1
            break

    # if no pivot found just reverse the array and return
    if pivot == -1:
        nums[:] = nums[::-1]
        return

    # find the next smallest Largest value than pivot
    for i in range(len(nums) - 1, pivot, -1):
        if nums[i] > nums[pivot]:
            # when found swap them
            print(nums[i])
            nums[i], nums[pivot] = nums[pivot], nums[i]
            break

    # reverse the array after pivot
    nums[pivot + 1 :] = nums[-1:pivot:-1]


nums = [1, 3, 2]
nextPermutation(nums)
print(nums)
