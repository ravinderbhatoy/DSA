from disjointSet import DisjointSet


def accountMerge(accounts: list[list[str]]) -> list[list[str]]:
    mapMailNode = {}  # mail -> node
    n = len(accounts)
    ds = DisjointSet(n)

    for i in range(n):
        for j in range(1, len(accounts[i])):
            mail = accounts[i][j]
            if mapMailNode.get(mail) is None:
                mapMailNode[mail] = i
            else:
                # if two accounts share common mail connect them
                ds.unionBySize(i, mapMailNode[mail])

    mergeMail = {i: [] for i in range(n)}

    for mail in mapMailNode:
        # find ultimate parent and append mails
        node = ds.find_parent(mapMailNode[mail])
        mergeMail[node].append(mail)

    mergeAccounts = []
    for node in mergeMail:
        if mergeMail[node]:
            mergeMail[node] = sorted(mergeMail[node])
            data = [accounts[node][0]]  # get the owner
            data.extend(mergeMail[node])  # add emails
            mergeAccounts.append(data)

    return mergeAccounts


accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"]]

print(accountMerge(accounts))
