from representation import tree_root, TreeNode


def checkBalance(root: TreeNode):

    def find_height(root):
        if root is None:
            return 0

        lh = checkBalance(root.left)
        rh = checkBalance(root.right)

        if lh == -1 or rh == -1:
            return -1

        if abs(lh - rh) > 1:
            return -1

        return 1 + max(lh, rh)

    return find_height(root) != -1


print(checkBalance(tree_root))
