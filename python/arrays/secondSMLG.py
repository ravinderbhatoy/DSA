def secondSmallest(nums: list[int]):
    smallest = float("inf")
    secondSmallest = float("inf")

    # finding smallest and second smallest
    for num in nums:
        if num < smallest:
            secondSmallest = smallest
            smallest = num
        elif num < secondSmallest and num != smallest:
            secondSmallest = num

    return secondSmallest


def secondLargest(nums: list[int]):
    # finding largest and second second largest
    largest = float("-inf")
    secondLargest = float("-inf")

    for num in nums:
        if num > largest:
            secondLargest = largest
            largest = num
        elif num > secondLargest and num != largest:
            secondLargest = num

    return secondLargest


nums = [1, 2, 4, 7, 7, 6]

secSm = secondSmallest(nums)
secLg = secondLargest(nums)

print(secSm, secLg)
