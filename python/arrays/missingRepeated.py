def findMissingAndRepeatedValues(grid: list[list[int]]) -> list[int]:
    n = len(grid)
    hash = [0] * (n * n + 1)

    for i in range(0, n):
        for j in range(0, n):
            hash[grid[i][j]] += 1

    missing = -1
    repeated = -1
    for i in range(1, len(hash)):
        if hash[i] == 0:
            missing = i
        elif hash[i] > 1:
            repeated = i

    return [repeated, missing]


grid = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
print(findMissingAndRepeatedValues(grid))
