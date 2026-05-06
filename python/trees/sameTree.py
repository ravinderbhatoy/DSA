from buildTree import build_tree


def is_same_tree(p, q):

    if not p and q:
        return False
    if not q and p:
        return False
    if not p and not q:
        return False

    def traverse(root):
        preorder = []

        def get_preorder(node):
            if not node:
                preorder.append(None)
                return
            preorder.append(node.val)
            get_preorder(node.left)
            get_preorder(node.right)

        get_preorder(root)
        return preorder

    tree1 = traverse(p)
    tree2 = traverse(q)

    print(tree1)
    print(tree2)
    return tree1 == tree2


def is_same_tree_rec(p, q):
    if not p and not q:
        return True

    if not p or not q or p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


p = build_tree([1, 2])
q = build_tree([1, None, 2])
print(is_same_tree_rec(p, q))
