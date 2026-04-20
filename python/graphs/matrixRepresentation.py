# adjancy matrix representation

def generate_matrix(n, edges: list[tuple]):
    adj_matrix = [[0] * (n + 1) for _ in range(n + 1)]

    for u, v in edges:
        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1

    for i in range(n + 1):
        print(adj_matrix[i])

    return adj_matrix


edges = int(input("Enter no. of edges: "))
vertices = int(input("Enter no. of vertices: "))

nodes = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (7, 8)]

# nodes = []
# for i in range(edges):
#     v = input("").split()
#     print(v)
#     first = int(v[0])
#     second = int(v[1])
#     nodes.append((first, second))


print(generate_matrix(vertices, nodes))
