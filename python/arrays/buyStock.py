def buyStock(prices):
    mini = prices[0]
    profit = 0

    for i in range(1, len(prices)):
        cost = prices[i] - mini
        profit = max(cost, profit)
        mini = min(prices[i], mini)

    return profit


print(buyStock([7, 1, 5, 3, 6, 4]))
