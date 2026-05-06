from buildTree import build_tree


def maxPathSum(root):
    # Use a list or nonlocal to track the global maximum
    max_sum = float('-inf')

    def find_max_gain(node):
        nonlocal max_sum
        if not node:
            return 0
        ls = max(find_max_gain(node.left), 0)
        rs = max(find_max_gain(node.right), 0)
        max_sum = max(max_sum, node.val + ls + rs)
        return node.val + max(ls, rs)

    find_max_gain(root)
    return max_sum


values = [-10, 9, 20, None, None, 15, 7]
root = build_tree(values)
print(maxPathSum(root))
