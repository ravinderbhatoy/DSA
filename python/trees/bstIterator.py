from representation import TreeNode, tree_root


class bstIterator:

    def __init__(self, root):
        self.stack = []
        self.pushAll(root.left)

    def next(self):
        node = self.stack.pop()
        self.pushAll(node.right)
        return node.val

    def hasNext(self):
        return True if len(self.stack) else False

    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.left


itr = bstIterator(tree_root)
print(itr.next())
print(itr.next())
print(itr.next())
