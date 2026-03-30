def concatenatedBinary(n) -> int:
    MOD = 10**9 + 7
    result = 0
    length = 0  # number of bits in current number

    for i in range(1, n + 1):
        # if i is power of 2, increase bit length
        if (i & (i - 1)) == 0:
            length += 1
        result = ((result << length) | i) % MOD
    return result


n = 5
print(concatenatedBinary(n))
