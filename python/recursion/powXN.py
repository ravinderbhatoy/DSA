def power(x, n):
    ans = 1
    while n > 0:
        if n % 2 == 1:
            ans *= x
        x *= x
        n = n // 2
    return ans


def powRec(x, n):
    if n == 0:
        return 1

    if n % 2 == 1:
        return x * powRec(x, n - 1)
    else:
        return powRec(x * x, n // 2)


print(power(2, 11))
