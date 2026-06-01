class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [0] * (n + 1)
        self.size = [1] * (n + 1)

        for i in range(n + 1):
            self.parent[i] = i

    def find_parent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        # find their ultimate parents
        upu = self.find_parent(u)
        upv = self.find_parent(v)

        # both are already attached
        if upv == upu:
            return

        # attach lower rank to higher
        if self.rank[upu] < self.rank[upv]:
            self.parent[upu] = upv
        elif self.rank[upv] < self.rank[upu]:
            self.parent[upv] = upu
        else:
            # both belong to same increase rank
            self.parent[upv] = upu
            self.rank[upu] += 1

    def unionBySize(self, u, v):
        upu = self.find_parent(u)
        upv = self.find_parent(v)

        if upv == upu:
            return

        if self.size[upu] < self.size[upv]:
            self.parent[upu] = upv
            # increase size of parent
            self.size[upv] += self.size[upu]
        else:
            self.parent[upv] = upu
            self.size[upu] += self.size[upv]


if __name__ == "__main__":
    ds = DisjointSet(7)
# ds.unionByRank(1, 2)
# ds.unionByRank(2, 3)
# ds.unionByRank(4, 5)
# ds.unionByRank(6, 7)
# ds.unionByRank(5, 6)
#

    print(ds.size)
    ds.unionBySize(1, 2)
    ds.unionBySize(2, 3)
    ds.unionBySize(4, 5)
    ds.unionBySize(6, 7)
    ds.unionBySize(5, 6)
    print(ds.size)


# is 3 and 7 same or not
    if ds.find_parent(3) == ds.find_parent(7):
        print("Same")
    else:
        print("Not same")

    ds.unionBySize(3, 7)

# is 3 and 7 same or not
    if ds.find_parent(3) == ds.find_parent(7):
        print("Same")
    else:
        print("Not same")
