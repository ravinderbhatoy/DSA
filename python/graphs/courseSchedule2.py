from collections import deque


def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    res = []
    queue = deque()
    indegree = [0] * numCourses

    preMap = {i: [] for i in range(numCourses)}

    # course, prerequisites
    for crs, prs in prerequisites:
        preMap[prs].append(crs)
        indegree[crs] += 1

    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        node = queue.popleft()

        res.append(node)

        for nei in preMap[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)

    return res if len(res) == numCourses else []


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

print(findOrder(numCourses, prerequisites))
