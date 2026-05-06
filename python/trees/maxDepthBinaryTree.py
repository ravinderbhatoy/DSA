from representation import tree_root, TreeNode


def maxDepth(root: TreeNode):
    if root is None:
        return 0

    lh = maxDepth(root.left)
    rh = maxDepth(root.right)

    return 1 + max(lh, rh)


print(maxDepth(tree_root))
