from representation import tree_root, TreeNode


def prePostInOrders(root: TreeNode):
    """
    Returns preorder, inorder, postorder traversal
    """
    if root is None:
        return [], [], []

    preorder = []
    inorder = []
    postorder = []

    stack = [(root, 1)]  # (node, num)

    while stack:
        node, num = stack.pop()
        if num == 1:
            preorder.append(node.val)
            stack.append((node, num + 1))
            if node.left:
                stack.append((node.left,  1))
        elif num == 2:
            inorder.append(node.val)
            stack.append((node, num + 1))
            if node.right:
                stack.append((node.right, 1))
        else:
            postorder.append(node.val)

    return preorder, inorder, postorder


preorder, inorder, postorder = prePostInOrders(tree_root)

print("Pre order:", preorder)
print("In order:", inorder)
print("Post order:", postorder)
