from representation import TreeNode
from collections import deque
from buildTree import build_tree


def rightSideView(root: TreeNode):
    # {'x': {'y': 'node'}}

    if root is None:
        return []

    que = deque([root])
    res = []

    while que:
        size = len(que)

        for i in range(size):
            node = que.popleft()

            if i == size - 1:
                # this is the last node from previous level
                res.append(node.val)

            if node.left:
                que.append((node.left))

            if node.right:
                que.append((node.right))
    return res


root = build_tree([1, 2, 3, 4, None, None, None, 5])
print(rightSideView(root))
