class StockSpanner:
    def __init__(self):
        self.stack = list()

    def next(self, price: int) -> int:
        # 1. Start with a span of 1 (today)
        span = 1

        # 2. Check previous days in the stack
        # If the previous price is smaller or equal, "swallow" its span
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        # 3. Push the current price and its TOTAL calculated span
        self.stack.append((price, span))


cmds = ["StockSpanner", "next", "next",
        "next", "next", "next", "next", "next"]

calls = [100, 80, 60, 70, 60, 75, 85]

obj = StockSpanner()
param = [0] * len(calls)

for i in range(len(calls)):
    param[i] = obj.next(calls[i])

print(param)
print(calls)
obj.show()
