from representation import TreeNode, tree_root


def findDiameter(root: TreeNode):
    """
    Width / diameter of tree
    """
    maxi = 0

    def find_height(root):
        nonlocal maxi
        if root is None:
            return 0

        lh = find_height(root.left)
        rh = find_height(root.right)
        maxi = max(maxi, lh + rh)

        return 1 + max(lh, rh)

    find_height(root)
    return maxi


print(findDiameter(tree_root))
