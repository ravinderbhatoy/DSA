from collections import deque


def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    ans = []
    dq = deque()

    for i in range(len(nums)):
        # check if element is part of window
        if dq and dq[0] <= i - k:
            dq.popleft()

        # remove any prior smaller or equal elements
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        dq.append(i)

        # occurence of window (first occurence is i == k - 1)
        if (i >= k - 1):
            ans.append(nums[dq[0]])

    return ans


nums = [1, 3, -1, -3, 5, 3, 6, 7]

print(maxSlidingWindow(nums, 3))
