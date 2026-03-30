def buyStock(prices):
    maxProfit = -1
    for i in range(len(prices)):
        profit = 0
        buy = prices[i]

        for j in range(i+1, len(prices)):
            if prices[j] > buy:
                profit = profit + prices[j] - buy
                break
        maxProfit = max(maxProfit, profit)
    return maxProfit


prices = [7, 1, 5, 3, 6, 4]
print(buyStock(prices))
