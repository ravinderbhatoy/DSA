from representation import TreeNode, tree_root


def countNode(root: TreeNode) -> int:
    """
    Count nodes in complete binary tree
    """

    if root is None:
        return 0

    def findLeftHeight(node):
        h = 0
        while node:
            h += 1
            node = node.left

        return h

    def findRighttHeight(node):
        h = 0
        while node:
            h += 1
            node = node.right

        return h

    lh = findLeftHeight(root)
    rh = findRighttHeight(root)

    if lh == rh:
        return (1 << lh) - 1

    return 1 + countNode(root.left) + countNode(root.right)


print(countNode(tree_root))
