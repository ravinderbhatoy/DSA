def nextGreaterElements(nums: int):
    stack = list()
    n = len(nums)
    ans = [0] * n

    for i in range(2 * n - 1, -1, -1):
        while len(stack) and stack[-1] <= nums[i % n]:
            stack.pop()

        if i < n:
            if len(stack) and stack[-1] > nums[i]:
                ans[i] = stack[-1]
            else:
                ans[i % n] = -1
        stack.append(nums[i % n])
    return ans


nums = [1, 2, 1]

print(nextGreaterElements(nums))
