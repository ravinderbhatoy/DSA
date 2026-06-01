from representation import TreeNode, tree_root


def findLcaOptimized(root: TreeNode, p: TreeNode, q: TreeNode):

    def get_lcs(node, p, q):
        if not node:
            return None

        if node == p or node == q:
            return root

        ls = get_lcs(node.left, p, q)
        rs = get_lcs(node.right, p, q)

        if not ls:
            return rs
        elif not rs:
            return ls

        return node

    return get_lcs(root, p, q)


def findLca(root: TreeNode, p: TreeNode, q: TreeNode):
    """
    Lowest common ancestor of p and q
    Approach:
    1. Find the path to p and q
    2. return last common node in two path
    """

    def findPath(node, target, path):
        if node is None:
            return False

        path.append(node)

        if node == target:
            print("Target found")
            return True  # no need to go further

        if (findPath(node.left, target, path)
                or findPath(node.right, target, path)):
            return True

        path.pop()
        return False

    ps_path = []
    qs_path = []

    findPath(root, p, ps_path)
    findPath(root, q, qs_path)

    lca = None
    for i in range(min(len(ps_path), len(qs_path))):
        if ps_path[i] == qs_path[i]:
            lca = ps_path[i]

    return lca


p = TreeNode(2)
q = TreeNode(5)

print(findLca(tree_root, p, q))
