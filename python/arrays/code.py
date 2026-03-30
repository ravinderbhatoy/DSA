def maxProfit(prices: list[int]) -> int:
    profit = 0
    mini = float("inf")
    maxi = 0
    for price in prices:
        mini = min(price, mini)
        profit = price - mini
        maxi = max(profit, maxi)

    return maxi


def generateSubArray(nums: [int]):
    for i in range(0, len(nums) - 1):
        for j in range(i, len(nums)):
            for n in range(i, j + 1):
                print(nums[n], end="")
            print(" ", end="")
        print("")


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
generateSubArray(prices)
