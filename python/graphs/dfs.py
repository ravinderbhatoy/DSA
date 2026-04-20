from listRepresentation import generate_adj_list


def dfs_traverse(start, n, adj_list):
    visited = [0] * (n + 1)
    res = []

    def dfs(node, adj_list):
        nonlocal visited, res
        visited[node] = 1
        res.append(node)

        for v in adj_list[node]:
            if not visited[v]:
                dfs(v, adj_list)

    dfs(start, adj_list)
    return res

# edges = int(input("Enter no. of edges: "))
# vertices = int(input("Enter no. of vertices: "))
#
#
# nodes = []
# for _ in range(edges):
#     values = input("").split()
#     u = int(values[0])
#     v = int(values[1])
#     nodes.append((u, v))
#


nodes_data = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (7, 8)]
edges = 7
nodes = 8
adj_list = generate_adj_list(nodes_data)

print(dfs_traverse(1, nodes, adj_list))
