from representation import tree_root, TreeNode


def isSymmetric(root: TreeNode):

    def traverse(left, right):
        if left.val != right.val:
            return False

        return (traverse(left.left, right.right)
                and traverse(left.right, right.left))

    return root is None or traverse(root.left, root.right)


print(isSymmetric(tree_root))
