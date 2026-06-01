from representation import TreeNode, bst_root


def kthSmallest(root: TreeNode, k: int) -> int:
    count, result = 0, -1

    def inOrder(node):
        nonlocal count, result

        if node is None or result != -1:
            return

        inOrder(node.left)
        count += 1

        if count == k:
            result = node.val
            return

        inOrder(node.right)

    inOrder(root)
    return result


print(kthSmallest(bst_root, 2))
