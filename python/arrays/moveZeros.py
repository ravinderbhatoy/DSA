def moveZeros(nums: list[int]):
    count = 0
    current = 0
    for i in range(0, len(nums)):
        if nums[i] == 0:
            count += 1
        else:
            nums[current] = nums[i]
            current += 1

    for i in range(len(nums) - count, len(nums)):
        nums[i] = 0
    return nums


def moveZerosOptimal(nums: list[int]):
    j = -1
    for i in range(0, len(nums)):
        if nums[i] == 0:
            j = i
            break

    for i in range(j + 1, len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return nums


nums = [0, 1, 0, 3, 12]
print(moveZeros(nums))
print(moveZerosOptimal(nums))
