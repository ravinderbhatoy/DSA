def radixSort(nums):

    def extract_digit(number, digit):
        while digit > 0:
            digit -= 1
            number //= 10
        return number % 10

    def countSort(nums, bit):
        # to count occurence of nums elements
        freq = [0] * 10
        size = len(nums)
        gap = 0
        ans = [0] * size
        for i in range(len(nums)):
            freq[extract_digit(nums[i], bit)] += 1

        # store cumulative frequency
        for i in range(1, len(freq)):
            freq[i] += freq[i-1]

        # decrement and reverse traverse
        for i in range(len(nums) - 1, -1, -1):
            ind = extract_digit(nums[i], bit)
            ans[freq[ind] - 1] = nums[i]
            freq[ind] -= 1
        nums[:] = ans

    if len(nums) == 1:
        return 0
    maxi = max(nums)
    bit = 0
    mGap = 0
    while (maxi > 0):
        countSort(nums, bit)
        maxi //= 10
        bit += 1

    for i in range(1, len(nums)):
        mGap = max(mGap, nums[i] - nums[i-1])

    return mGap


nums = [3, 6, 9, 1]
print(radixSort(nums))
print(nums)
