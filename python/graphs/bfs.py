from listRepresentation import generate_adj_list
from collections import deque


def bfs_travers(start: int, n: int, adj_list) -> list[int]:
    visited = [0] * (n + 1)  # assuming 1 base indexing
    q = deque()
    res = []

    visited[start] = 1
    q.append(start)
    res.append(start)

    while q:
        v = q.popleft()
        nodes = adj_list[v]
        for node in nodes:
            if not visited[node]:
                visited[node] = 1
                q.append(node)
                res.append(node)

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

print(bfs_travers(1, nodes, adj_list))
