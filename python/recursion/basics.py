def count(n):
    if n == 0:
        return 0
    count(n - 1)
    print(n)


def reverseCount(n):
    if n == 0:
        return
    print(n)
    reverseCount(n - 1)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def sumOfN(n):
    if n == 1:
        return 1
    return n + sumOfN(n - 1)


print(sumOfN(5))
