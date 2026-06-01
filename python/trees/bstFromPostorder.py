from representation import TreeNode


def bstFromPostOrder(postorder: list[int]) -> TreeNode:
    inorder = sorted(postorder)

    inMap = {value: i for i, value in enumerate(inorder)}

    def build_tree(in_start, in_end, post_start, post_end):
        if in_start > in_end or post_start > post_end:
            return None

        root_val = postorder[post_end]
        root = TreeNode(root_val)

        index = inMap[root_val]
        nums_left = index - in_start

        root.left = build_tree(in_start, index - 1,
                               post_start, post_start + nums_left - 1)

        root.right = build_tree(index + 1, in_end,
                                post_start + nums_left, post_end - 1)

        return root

    n = len(postorder) - 1
    root = build_tree(0, n, 0, n)
    return root


postorder = [20, 40, 30, 60, 50, 10]
root = bstFromPostOrder(postorder)
print(root)
