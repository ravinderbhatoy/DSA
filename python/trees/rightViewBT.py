from representation import TreeNode
from collections import deque, defaultdict
from buildTree import build_tree


def rightSideView(root: TreeNode):
    # {'x': {'y': 'node'}}
    nodes = defaultdict(int)
    que = deque([(root, 0, 0)])

    while que:
        size = len(que)

        for i in range(size):
            node, x, lev = que.popleft()

            nodes[lev] = node.val
            if node.left:
                que.append((node.left, x - 1, lev + 1))

            if node.right:
                que.append((node.right, x + 1, lev + 1))

    res = []
    print(nodes.keys())
    for lev in sorted(nodes.keys()):
        res.append(nodes[lev])

    return res


root = build_tree([1, 2, 3, 4, None, None, None, 5])
print(rightSideView(root))
