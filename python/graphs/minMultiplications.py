from collections import deque


def minSteps(arr, start, end):
    mod = 1000
    dist = [float('inf')] * mod

    q = deque([[start, 0]])  # node, steps
    dist[start] = 0

    while q:
        node, steps = q.popleft()

        for num in arr:
            value = (node * num) % mod
            if value == end:
                return steps + 1

            if steps + 1 < dist[value]:
                dist[value] = steps + 1
                q.append([value, steps + 1])

    return -1


arr = [2, 5, 7]
start = 3
end = 30

print(minSteps(arr, start, end))
