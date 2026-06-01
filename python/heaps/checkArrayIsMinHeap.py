def check(nums: list[int]) -> bool:
    for i in range(len(nums) // 2):
        left = 2 * i + 1
        right = 2 * i + 2
        # compare with left and right child
        if nums[i] > nums[left] or nums[i] > nums[right]:
            return False
    return True


nums = [10, 20, 30, 25, 15]
print(check(nums))
