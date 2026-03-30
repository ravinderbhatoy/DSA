def kthPermutation(n: int, k: int):
    fact = 1
    numbers = []
    for i in range(1, n):
        numbers.append(i)
        fact = fact * i
    # insert last number
    numbers.append(n)
    ans = ""
    k = k - 1  # 0 base indexing 17th permutation will be 16th

    while (True):
        ans = ans + str(numbers[k // fact])
        numbers.pop(k // fact)
        if len(numbers) == 0:
            break

        k = k % fact
        fact = fact // len(numbers)

    return ans


print(kthPermutation(4, 17))
