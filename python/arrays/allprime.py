N = int(input())

# sieve of eratosthenes

prime = [1] * (N + 1)

for i in range(2, N+1):
    if prime[i]:
        for j in range(i*i, N+1, i):
            prime[j] = 0

for i in range(2, len(prime)):
    if prime[i]:
        print(i)
