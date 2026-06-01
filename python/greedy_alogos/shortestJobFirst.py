def avgExecutionTime(bt: list[int]) -> int:
    bt = sorted(bt)
    totalbt = 0

    prefixSum = bt[0]

    for i in range(1, len(bt)):
        totalbt += prefixSum
        prefixSum += bt[i]

    return totalbt // len(bt)


bt = [4, 3, 7, 1, 2]
print(avgExecutionTime(bt))
