from buildTree import build_tree
from collections import deque


def minDiffInBST(root):
    mini = float('inf')

    prev = None

    def inorder(node):
        nonlocal mini, prev
        if not node:
            return

        inorder(node.left)
        if prev:
            mini = min(mini, node.val - prev.val)
        prev = node
        inorder(node.right)

    inorder(root)
    return mini


root = build_tree([1, 0, 48, None, None, 12, 49])
print(minDiffInBST(root))
