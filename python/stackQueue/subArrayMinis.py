def sumSubArrayMins(nums: list[int]) -> int:
    def findNSE(nums):
        """
        Find next smallest element
        """
        stack = list()
        n = len(nums)
        ans = [n] * n

        for i in range(n-1, -1, -1):
            while len(stack) and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if len(stack):
                ans[i] = stack[-1]

            stack.append(i)

        return ans

    def findPSEE(nums):
        """
        Find previous smallest of equal element
        """
        stack = list()
        n = len(nums)
        ans = [-1] * n

        for i in range(n):
            while len(stack) and nums[stack[-1]] > nums[i]:
                stack.pop()

            if len(stack):
                ans[i] = stack[-1]

            stack.append(i)

        return ans

    PSEE = findPSEE(nums)
    NSE = findNSE(nums)
    total = 0
    mod = 1e9 + 7

    print(PSEE)
    print(NSE)

    for i in range(len(nums)):
        left = i - PSEE[i]
        right = NSE[i] - i

        freq = left * right
        val = (freq * nums[i])
        total += val % mod

    return int(total)


nums = [3, 1, 2, 4]

print(sumSubArrayMins(nums))
