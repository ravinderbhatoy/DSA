def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    preMap = {i: [] for i in range(numCourses)}

    for crs, prs in prerequisites:
        preMap[crs].append(prs)

    # just detect whether or not there is a cycle
    # if cycle exist not possible to finish courses

    visited = [0] * numCourses
    path_visited = [0] * numCourses

    print(preMap)

    def dfs(node, parent):
        visited[node] = 1
        path_visited[node] = 1

        # a course without any prerequisites
        if preMap[node] == []:
            return True

        for nei in preMap[node]:
            if not visited[nei]:
                if dfs(nei):
                    return True

            elif path_visited[nei]:
                # it has to be on the same path
                return True

        path_visited[node] = 0  # for upcoming nodes path
        return False

    for i in range(numCourses):
        if not visited and dfs(i, -1):
            return True

    return False


numCourses = 2
prerequisites = [[1, 0]]

print(canFinish(numCourses, prerequisites))
