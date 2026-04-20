
def canFinish(numCourses: int, prerequisites: list[list[int]]):
    preMap = {i: [] for i in range(numCourses)}

    for cre, pre in prerequisites:
        preMap[cre].append(pre)

    visited = set()

    def dfs(crs):
        if crs in visited:
            return False
        # a course without any prerequisites
        if preMap[cre] == []:
            return True

        visited.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre):
                return False

        visited.remove(crs)
        preMap[cre] = []  # to remember we have check it

        return True

    for crs in range(numCourses):
        if not dfs(crs):
            return False

    return True


numCourses = 2
prerequisites = [[1, 0]]
print(canFinish(numCourses, prerequisites))
