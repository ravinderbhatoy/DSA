from collections import defaultdict, deque


def alienDicionary(words: list[str]) -> str:
    n = len(words)
    unique_chars = set("".join(words))
    adjacency = defaultdict(list)
    indegree = {char: 0 for char in unique_chars}

    # create adjacency list by comparing
    for i in range(n - 1):
        s1 = words[i]
        s2 = words[i+1]

        size = min(len(s1), len(s2))
        for k in range(size):
            if s1[k] != s2[k]:
                # a -> b or vice versa
                adjacency[s1[k]].append(s2[k])
                indegree[s2[k]] += 1
                break

        if len(s1) > len(s2) and s1[:size] == s2[:size]:
            return ""

    queue = deque()

    for char in indegree:
        if indegree[char] == 0:
            queue.append(char)

    res = []
    while queue:
        node = queue.popleft()
        res.append(node)
        for nei in adjacency[node]:
            indegree[nei] -= 1
            if not indegree[nei]:
                queue.append(nei)

    if len(res) < len(unique_chars):
        return ""

    return "".join(res)


words = ["baa", "abcd", "abca", "cab", "cad"]

print(alienDicionary(words))
