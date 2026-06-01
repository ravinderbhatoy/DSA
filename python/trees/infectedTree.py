from representation import TreeNode
from collections import deque
from buildTree import build_tree


def amountOfTime(root: TreeNode, start: TreeNode) -> int:

    # def search(root, target):
    #     if root is None:
    #         return
    #
    #     if root.val == target:
    #         return root
    #
    #     left_res = search(root.left, target)
    #     if left_res:
    #         return left_res
    #     return search(root.right, target)

    # get parents
    queue = deque([root])
    parents = {}
    source = None

    while queue:
        node = queue.popleft()

        if node.val == start:
            source = node

        if node.left:
            parents[node.left] = node
            queue.append(node.left)
        if node.right:
            parents[node.right] = node
            queue.append(node.right)

    queue = deque([source])
    visited = {source}
    time = 0

    while queue:
        flag = 0
        for _ in range(len(queue)):
            node = queue.popleft()
            for neighbour in [parents.get(node), node.left, node.right]:
                if neighbour and neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
                    flag = 1

        if flag:
            time += 1
    return time


root = build_tree([1, 5, 3, None, 4, 10, 6, 9, 2])
print(amountOfTime(root, root.right.val))
