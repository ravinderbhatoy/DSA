from representation import tree_root, TreeNode
from collections import deque, defaultdict
from buildTree import build_tree


def topView(root: TreeNode):
    nodes = defaultdict(int)
    que = deque()
    que.append((root, 0, 0))  # (node, x , y)

    while que:
        size = len(que)

        for i in range(size):
            node, x, y = que.popleft()
            if not nodes[x]:
                nodes[x] = node.val

            if node.left:
                que.append((node.left, x - 1, y + 1))

            if node.right:
                que.append((node.right, x + 1, y + 1))

    res = []
    print(nodes.keys())
    for x in sorted(nodes.keys()):
        res.append(nodes[x])
    return res


root = build_tree([6, None, 2, 8, 3, 4])

print(topView(tree_root))
