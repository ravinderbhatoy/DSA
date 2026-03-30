# doubly ended queue
from collections import deque


def maxSlidingWindow(nums: [int], k: int):
    # queue will store valid max values
    q = deque()
    ans = []
    for i in range(k):
        # find max element for first window
        while (len(q) > 0 and nums[q[-1]] <= nums[i]):
            q.pop()
        q.append(i)

    for i in range(k, len(nums)):
        ans.append(nums[q[0]])
        # if front element is out of window
        if q[0] <= i-k:
            q.popleft()

        while (len(q) > 0 and nums[q[-1]] <= nums[i]):
            q.pop()
        q.append(i)

    ans.append(nums[q[0]])
    return ans


nums = [1, 3, -1, -3, 5, 3, 6, 7]
print(maxSlidingWindow(nums, 3))
