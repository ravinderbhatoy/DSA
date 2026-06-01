def maximumUnits(boxTypes: list[list[int]], truckSize: int) -> int:
    """
    boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]
    We want maximumUnits in minimum no. of boxes
    """

    boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
    units = 0

    for boxSize, unit in boxTypes:
        if truckSize >= boxSize:
            units += boxSize * unit
            truckSize -= boxSize
        else:
            units += truckSize * unit
            break

    return units


boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
truckSize = 10
print(maximumUnits(boxTypes, truckSize))
