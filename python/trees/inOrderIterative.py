from representation import TreeNode, tree_root


def inOrderTraversal(root: TreeNode):
    res = []
    if root is None:
        return res

    stack = []
    node = root
    # unless stack is empty
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        res.append(node.val)
        node = node.right

    return res


if __name__ == "__main__":
    print(inOrderTraversal(tree_root))
