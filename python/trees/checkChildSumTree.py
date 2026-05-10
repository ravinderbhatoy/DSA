from representation import TreeNode


def checkTree(root: TreeNode) -> bool:
    return root.val == (root.left.val + root.right.val)


root = TreeNode(5)
root.right = TreeNode(15)
root.left = TreeNode(-10)

print(checkTree(root))
