from collections import defaultdict


def generate_adj_list(edges: list[tuple], undirected=True):
    # defaultdict handles missing keys automatically
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        if undirected:
            adj_list[v].append(u)

    return dict(adj_list)


# Your data

if __name__ == "__main__":
    print("Inside main file")
    nodes = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (7, 8)]

    adj_list = generate_adj_list(nodes)

# Displaying the list
    for vertex, neighbors in adj_list.items():
        print(f"{vertex}: {neighbors}")
