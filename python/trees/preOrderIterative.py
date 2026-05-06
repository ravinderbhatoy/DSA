from representation import tree_root, TreeNode


def pre_order_traverse(root: TreeNode):
    """
    order -> Root, left, right
    """
    res = []
    if root is None:
        return res
    stack = []
    stack.append(root)

    while stack:
        t_node = stack.pop()
        res.append(t_node.val)

        if t_node.right is not None:
            stack.append(t_node.right)
        # bcz of LIFO left will be poped out first
        # so later insertion (last in first out)
        if t_node.left is not None:
            stack.append(t_node.left)

    return res
