from representation import TreeNode, bst_root


def findTarget(root: TreeNode, k: int) -> bool:
    mpp = {}
    res = []

    def traverse(root):
        nonlocal mpp, k, res
        if root is None:
            return

        traverse(root.left)
        res.append(root.val)
        traverse(root.right)

    traverse(root)
    s, e = 0, len(res) - 1

    while s <= e:
        sum = res[s] + res[e]
        if sum == k:
            return True
        if sum > k:
            e -= 1
        else:
            s += 1

    return False


print(findTarget(bst_root, 13))
