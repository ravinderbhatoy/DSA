from collections import deque


def smallestSubarray(nums: list[int], k: int) -> int:
    minWindowSize = float('inf')
    windowStart = 0
    currentWindowSum = 0

    for windowEnd in range(len(nums)):

        currentWindowSum += nums[windowEnd]
        while (currentWindowSum >= k):
            minWindowSize = min(minWindowSize, windowEnd - windowStart + 1)
            # it can't be reduced further
            if minWindowSize == 1:
                return minWindowSize
            currentWindowSum -= nums[windowStart]
            windowStart += 1

    return minWindowSize if minWindowSize != float('inf') else -1


def smallestSubarrayWithNegatives(nums: list[int], k: int) -> int:
    res = float('inf')
    dq = deque()
    curr_sum = 0

    for r in range(len(nums)):
        curr_sum += nums[r]

        if curr_sum >= k:
            res = min(res, r + 1)

        while dq and curr_sum - dq[0][0] >= k:
            prefix, end_idx = dq.popleft()  # from left (start)
            res = min(res, r - end_idx)

        # keep monotonic
        while dq and dq[-1][0] >= curr_sum:
            dq.pop()  # from right

        dq.append((curr_sum, r))

    return -1 if res == float('inf') else res


nums = [84, -37, 32, 40, 95]
k = 167

print(smallestSubarray(nums, k))
print(smallestSubarrayWithNegatives(nums, k))
