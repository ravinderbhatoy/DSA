def isPrime(num):
    i = 2
    while i * i < num:
        if num % i == 0:
            return "Not prime"
        i += 1
    return "Prime"


def countPrime(num):
    # no. of primes upto num
    count = 0
    isPrime = [1] * (num + 1)
    print(isPrime)
    for i in range(2, num):
        if isPrime[i]:
            count += 1
            for j in range(i * 2, num, i):
                isPrime[j] = 0

    return count


def countDigit(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1

    return count


def sumOfDigits(num):
    sm = 0
    while num > 0:
        digit = num % 10
        sm += digit
        num = num // 10
    return sm


def findGCD(a, b):
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd


def findGCD2(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    if a == 0:
        return b
    else:
        return a


def gcdRec(a, b):
    if b == 0:
        return a
    return gcdRec(b, a % b)


def lcm(a, b):
    gcd = gcdRec(a, b)
    return a * b / gcd


def reverseNumber(num):
    ans = 0
    while num > 0:
        digit = num % 10
        num = num // 10
        ans *= 10
        ans += digit
    return ans


# print(isPrime(12))
print(findGCD(0, 24))
print(reverseNumber(234567))
print(findGCD2(6, 10))
print(gcdRec(6, 10))
print(lcm(20, 28))
