from representation import TreeNode, tree_root
from collections import deque


def distanceK(root: TreeNode, target: TreeNode, k: int):
    parents = {}
    # get parents for all the nodes
    # to traverse in all directions

    queue = deque([root])
    # O(N)
    while queue:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
            parents[node.left] = node
        if node.right:
            queue.append(node.right)
            parents[node.right] = node

    queue = deque([target])
    visited = {target}
    curr_dis = 0

    # start moving and calculate distance
    # O(N)
    while queue:
        if curr_dis == k:
            return [node.val for node in queue]

        for _ in range(len(queue)):
            node = queue.popleft()
            for neighbor in [node.left, node.right, parents.get(node)]:
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        curr_dis += 1

    return []


print(distanceK(tree_root, tree_root.right, 2))
