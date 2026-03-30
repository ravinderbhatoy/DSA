# raise x to power n
def pow(x: float, n: int):
    binForm = n
    ans = 1
    if n < 0:
        x = 1 / x
        binForm = -binForm
    while binForm > 0:
        if binForm % 2 == 1:
            ans = ans * x
        x = x * x
        binForm = binForm // 2
    return ans


print(pow(2.0, 2))
