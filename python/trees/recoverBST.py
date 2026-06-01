from representation import TreeNode
from morisTraversal import inorder
from buildTree import build_tree


def recoverTree(root: TreeNode):
    prev = first = second = None

    def inorder(node):
        nonlocal prev, first, second

        if node is None:
            return

        inorder(node.left)

        if prev and node.val < prev.val:
            if not first:
                first = prev
            second = node
        prev = node
        inorder(node.right)

    inorder(root)
    first.val, second.val = second.val, first.val


values = [3, 1, 4, None, None, 2]
root = build_tree(values)
print(recoverTree(root))
print(inorder(root))
