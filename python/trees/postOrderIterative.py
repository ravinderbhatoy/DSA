from representation import tree_root, TreeNode


def postOrderTraversal(root: TreeNode):
    """
    Uses 2 stacks
    """
    if root is None:
        return []

    # stack 1 and stack 2
    s1 = []
    s2 = []

    s1.append(root)

    while s1:
        node = s1.pop()
        s2.append(node.val)

        if node.left:
            s1.append(node.left)

        if node.right:
            s1.append(node.right)

    return s2[::-1]


def postOrderTraversal1(root: TreeNode):
    """
    Uses 1 stacks
    """
    stack = []
    res = []
    curr = root

    while curr or stack:
        # go as left as possible
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            # move right if possible
            temp = stack[-1].right
            # if no right
            if temp is None:
                temp = stack.pop()
                res.append(temp.val)
                while stack and temp is stack[-1].right:
                    temp = stack.pop()
                    res.append(temp.val)
            else:
                curr = temp
    return res


print(postOrderTraversal1(tree_root))
