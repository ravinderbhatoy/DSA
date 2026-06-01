from representation import bst_root, tree_root
from collections import deque


def isValidBST(root):
    if not root:
        return True

    queue = deque([(root, float('-inf'), float('inf'))])
    # (node, lower_bound, upper_bound)

    while queue:
        node, low, high = queue.popleft()

        # between range(lower_bound - upper_bound) check
        if not (low < node.val < high):
            return False

        if node.left:
            # going left update upper_bound
            queue.append((node.left, low, node.val))

        if node.right:
            # going right update lower_bound
            queue.append((node.right, node.val, high))

    return True


def isValid(root):
    def check(root, low, high):
        if not root:
            return True

        if not (low < root.val < high):
            return False

        return (check(root.left, low, root)
                and check(root.right, root.val, high))

    return check(root, float('-inf'), float('inf'))


print(isValidBST(tree_root))
print(isValidBST(bst_root))
