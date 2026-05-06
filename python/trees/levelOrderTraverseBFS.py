from representation import TreeNode
from collections import deque


def levelOrder(root: TreeNode):
    res = []
    if root is None:
        return res

    queue = deque([(root)])

    while queue:
        size = len(queue)

        level = []
        for i in range(size):
            tree_node = queue.popleft()
            if tree_node.left:
                queue.append(tree_node.left)
            if tree_node.right:
                queue.append(tree_node.right)
            level.append(tree_node.val)

        res.append(level)

    return res


# creating tree
tree_root = TreeNode(1)
tree_root.left = TreeNode(2)
tree_root.right = TreeNode(3)
tree_root.left.left = TreeNode(4)
tree_root.left.right = TreeNode(5)
tree_root.right.right = TreeNode(7)
tree_root.right.left = TreeNode(6)

res = levelOrder(tree_root)
print(res)
