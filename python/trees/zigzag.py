from buildTree import build_tree
from collections import deque


def zigzaglevelorder(root) -> list[list[int]]:
    res = []
    if root is None:
        return res

    queue = deque([(root)])
    left_to_right = True

    while queue:
        size = len(queue)
        level = [0] * size
        for i in range(size):
            tree_node = queue.popleft()

            if left_to_right:
                level[size - 1 - i] = tree_node.val
            else:
                level[i] = tree_node.val

            if tree_node.left:
                queue.append(tree_node.left)
            if tree_node.right:
                queue.append(tree_node.right)

        left_to_right = not left_to_right
        res.append(level)
    return res


root = build_tree([3, 9, 20, None, None, 15, 7])
print(zigzaglevelorder(root))
