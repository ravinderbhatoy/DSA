from collections import deque
from representation import TreeNode, tree_root


def maxWidth(root: TreeNode):
    queue = deque([{"node": root, "idx": 0}])  # node, index
    maxi = 0

    while queue:
        size = len(queue)
        mini = queue[0]['idx']
        first = last = 0
        for i in range(size):
            curr_idx = queue[0]['idx'] - mini
            node = queue.popleft()['node']

            if i == 0:
                first = curr_idx
            if i == size - 1:
                last = curr_idx

            if node.left:
                queue.append({'node': node.left, 'idx': curr_idx*2+1})
            if node.right:
                queue.append({'node': node.left, 'idx': curr_idx*2+2})

        maxi = max(maxi, last - first + 1)

    return maxi


print(maxWidth(tree_root))
