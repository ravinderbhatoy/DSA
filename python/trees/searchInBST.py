from representation import bst_root
from collections import deque


def searchBST(root, val: int):
    res = []
    while (root and root.val != val):
        root = root.left if root.val > val else root.right

    # print subtree rooted to target node
    if root:
        queue = deque([root])

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

    return res


print(searchBST(bst_root, 12))
