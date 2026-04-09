
class Solution:

    def subArrayRanges(self, nums: list[int]) -> int:
        n = len(nums)
        sm = self.subArrayMaxs(nums, n) - self.subArrayMins(nums, n)
        return sm

    def findNSE(self, nums, n):
        stack = list()
        nse = [n] * n

        for i in range(n-1, -1, -1):
            while len(stack) and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if len(stack):
                nse[i] = stack[-1]

            stack.append(i)
        return nse

    def findNGE(self, nums, n):
        stack = list()
        nge = [n] * n

        for i in range(n-1, -1, -1):
            while len(stack) and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if len(stack):
                nge[i] = stack[-1]

            stack.append(i)
        return nge

    def findPSEE(self, nums, n):
        stack = list()
        psee = [-1] * n

        for i in range(n):
            while len(stack) and nums[stack[-1]] > nums[i]:
                stack.pop()

            if len(stack):
                psee[i] = stack[-1]

            stack.append(i)
        return psee

    def findPGEE(self, nums, n):
        stack = list()
        pgee = [-1] * n

        for i in range(n):
            while len(stack) and nums[stack[-1]] < nums[i]:
                stack.pop()

            if len(stack):
                pgee[i] = stack[-1]

            stack.append(i)
        return pgee

    def subArrayMaxs(self, nums, n):
        NGE = self.findNGE(nums, n)
        PGEE = self.findPGEE(nums, n)
        total = 0
        for i in range(n):
            left = i - PGEE[i]
            right = NGE[i] - i

            freq = left * right
            val = freq * nums[i]
            total += val

        return total

    def subArrayMins(self, nums, n):
        NGE = self.findNSE(nums, n)
        PGEE = self.findPSEE(nums, n)
        total = 0
        for i in range(n):
            left = i - PGEE[i]
            right = NGE[i] - i

            freq = left * right
            val = freq * nums[i]
            total += val

        return int(total)


nums = [1, 2, 3]
sol = Solution()
print(sol.subArrayRanges(nums))
