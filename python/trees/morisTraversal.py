from representation import TreeNode, tree_root


def inorder(root: TreeNode) -> list[int] | None:
    curr = root
    res = []
    while curr:
        # extream left node
        if curr.left is None:
            res.append(curr.val)
            curr = curr.right
        else:
            prev = curr.left
            # inorder predecessor
            while prev.right and prev.right != curr:
                prev = prev.right
            # attach thread to predecessor
            if prev.right is None:
                prev.right = curr
                curr = curr.left
            else:
                # remmove thread
                prev.right = None
                res.append(curr.val)
                curr = curr.right

    return res


def preorder(root: TreeNode) -> list[int] | None:
    curr = root
    res = []
    while curr:
        if curr.left is None:
            res.append(curr.val)
            curr = curr.right
        else:
            prev = curr.left

            while prev.right and prev.right != curr:
                prev = prev.right

            if prev.right is None:
                prev.right = curr
                res.append(curr.val)
                curr = curr.left
            else:
                prev.right = None
                curr = curr.right

    return res


if __name__ == "__main__":
    print(inorder(tree_root))
