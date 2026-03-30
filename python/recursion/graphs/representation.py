n = int(input("Enter n: "))
m = int(input("Enter m: "))

matrix = [[0] * (n+1) for _ in range(m+1)]

for i in range(m):
    u = int(input("Enter u: "))
    v = int(input("Enter v: "))

    matrix[u][v] = 1
    matrix[v][u] = 1

print(matrix)
