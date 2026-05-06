from representation import tree_root, TreeNode
from collections import deque
from buildTree import build_tree


def bottomView(root: TreeNode):
    nodes = {}
    que = deque()
    que.append((root, 0, 0))  # (node, x , y)

    while que:
        size = len(que)

        for i in range(size):
            node, x, y = que.popleft()
            # last level node of every axis
            nodes[x] = node.val

            if node.left:
                que.append((node.left, x - 1, y + 1))

            if node.right:
                que.append((node.right, x + 1, y + 1))

    res = []
    for x in sorted(nodes.keys()):
        res.append(nodes[x])
    return res


root = build_tree([6, None, 2, 8, 3, 4])

print(bottomView(tree_root))
