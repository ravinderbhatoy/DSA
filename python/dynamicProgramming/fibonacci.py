calls = 0


def fibonacci(n, dp):
    global calls
    if n <= 1:
        return n

    if dp[n] != -1:
        calls += 1
        return dp[n]
    return fibonacci(n - 1, dp) + fibonacci(n - 2, dp)


n = 20
dp = [-1] * (n + 1)
# ************ TC -> O(N) / SC -> O(2N) ************
# for i in range(0, n):
#     val = fibonacci(i, dp)
#     dp[i] = val
#     print(val)
#
# print("Calls saved:", calls)


# Tabulation
# ************ TC -> O(N) / SC -> O(N) ************
# dp = [-1] * (n + 1)
# dp[0] = 0
# dp[1] = 1
#
# for i in range(2, n):
#     dp[i] = dp[i-2] + dp[i-1]
#     print(dp[i])


# ************ TC -> O(N) / SC -> O(1) ************
prev = 1
prev2 = 0
n = 8
for i in range(2, n+1):
    val = prev + prev2
    prev2 = prev
    prev = val

print(prev)
