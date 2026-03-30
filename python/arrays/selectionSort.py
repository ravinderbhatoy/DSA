# find smallest each time and place it at correct position
def selectionSort(nums):
    for i in range(len(nums)):
        sm = i
        for j in range(i, len(nums)):
            if nums[sm] > nums[j]:
                sm = j
        nums[sm], nums[i] = nums[i], nums[sm]

    return nums


# swap adjacent elements
def bubbleSort(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


# compare curent element with its predecessors
def insertionSort(nums):
    # first element is assumed to be sorted
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums


nums = [11, 12, 25, 22, 9]
print(selectionSort(nums))
print(bubbleSort(nums))
print(insertionSort(nums))
