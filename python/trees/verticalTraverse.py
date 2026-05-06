from collections import deque, defaultdict
from representation import tree_root, TreeNode


def vertical_traverse(root: TreeNode):
    nodes = defaultdict(lambda: defaultdict(list))
    que = deque()
    que.append((root, 0, 0))  # (node, x , y)

    while que:
        size = len(que)

        for i in range(size):
            node, x, y = que.popleft()
            nodes[x][y].append(node.val)
            nodes[x][y] = sorted(nodes[x][y])

            if node.left:
                que.append((node.left, x - 1, y + 1))

            if node.right:
                que.append((node.right, x + 1, y + 1))

    res = []
    for x in sorted(nodes.keys()):
        column = []
        for y in sorted(nodes[x].keys()):
            column.extend(sorted(nodes[x][y]))
        res.append(column)
    return res


print(vertical_traverse(tree_root))
