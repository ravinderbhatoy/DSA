from representation import bst_root, TreeNode


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode):
    if root is None:
        return None
    if root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)
    if root.val > q.val and root.val > p.val:
        return lowestCommonAncestor(root.left, p, q)
    return root


print(lowestCommonAncestor(bst_root.left.right,
      bst_root.left.right, bst_root.left.left))
