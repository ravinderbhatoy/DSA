from representation import tree_root, TreeNode


def get_paths(root: TreeNode):
    if not root:
        return []

    res = []

    def find_path(node, path):
        nonlocal res
        path.append(str(node.val))

        # Check if it's a LEAF node
        if not node.left and not node.right:
            res.append("->".join(path))  # Copy the current path
        else:
            # If not a leaf, keep exploring
            if node.left:
                find_path(node.left, path)
            if node.right:
                find_path(node.right, path)

        # Backtrack: remove current node before going back up
        path.pop()

    find_path(root, [])
    return res


print(get_paths(tree_root))
