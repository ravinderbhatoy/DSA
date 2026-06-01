from representation import TreeNode
from buildTree import build_tree
from inOrderIterative import inOrderTraversal
from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return ""

        encoded = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if not node:
                encoded.append('x')
            else:
                encoded.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        # Join with commas. Clean and simple.
        return ",".join(encoded)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data:
            return None

        # Split the string into an easily iterable list
        values = data.split(',')

        root = TreeNode(int(values[0]))
        queue = deque([root])

        # Use an index pointer to read through the 'values' list
        idx = 1

        while queue and idx < len(values):
            node = queue.popleft()

            # Process Left Child
            if values[idx] != 'x':
                node.left = TreeNode(int(values[idx]))
                queue.append(node.left)
            else:
                node.left = None
            idx += 1  # Move to the next value in the list

            # Process Right Child
            if idx < len(values) and values[idx] != 'x':
                node.right = TreeNode(int(values[idx]))
                queue.append(node.right)
            else:
                node.right = None
            idx += 1  # Move to the next value in the list

        return root


ser = Codec()
deser = Codec()
root = build_tree([1, 2, 3, None, None, 4, 5])
ans = deser.deserialize(ser.serialize(root))
print(inOrderTraversal(ans))
