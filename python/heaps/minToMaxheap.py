def convert(nums: list[int]):
    n = len(nums)

    def max_heapify(nums, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < n and nums[left] > nums[largest]:
            largest = left

        if right < n and nums[right] > nums[largest]:
            largest = right

        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            max_heapify(nums, largest)

    # travers all non-leaf nodes
    for i in range(len(nums) // 2 - 1, -1, -1):
        max_heapify(nums, i)


nums = [10, 20, 30, 25, 15]
convert(nums)
print(nums)
