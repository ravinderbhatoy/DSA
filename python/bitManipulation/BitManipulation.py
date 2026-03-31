# swap 2 numbers
a = 5
b = 10

a = a ^ b
b = a ^ b
a = a ^ b


# set the ith bit
n = 13
i = 1

n = n | (1 << i)

# clear ith bit
n = 15
i = 1
n = n & ~(1 << i)
print(n)
