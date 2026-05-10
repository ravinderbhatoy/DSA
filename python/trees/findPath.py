from representation import tree_root, TreeNode


def get_path(root: TreeNode, target):
    res = []

    def find_path(node, target):
        nonlocal res
        if node is None:
            return False

        res.append(node.val)

        if node.val == target:
            return True

        if (find_path(node.left, target) or find_path(node.right, target)):
            return True

        res.pop()
        return False

    find_path(root, target)
    return res


print(get_path(tree_root, 7))
