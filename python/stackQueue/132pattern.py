def find132Pattern(nums) -> bool:
    n = len(nums)
    stack = list()  # pair [num, minLeft]
    currMin = nums[0]

    for n in nums[1:]:
        while stack and stack[-1][0] <= n:
            stack.pop()

        if stack and n > stack[-1][1]:
            return True

        stack.append([n, currMin])
        currMin = min(currMin, n)

    return False


nums = [1, 0, 1, -4, -3]
print(find132Pattern(nums))
