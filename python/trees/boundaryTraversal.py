from representation import tree_root


class Solution:
    def __init__(self):
        self.res = []

    def isLeaf(self, node):
        """Checks whether a node is leaf or not"""
        if not node.left and not node.right:
            return True
        return False

    def add_left_boundary(self, root):
        """Traverse left boundary excluding leafs"""
        node = root.left

        while node:
            if not self.isLeaf(node):
                self.res.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right

    def add_right_boundary(self, root):
        """Traverse right boundary excluding leafs"""
        node = root.right
        temp = []
        while node:
            if not self.isLeaf(node):
                temp.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left

        for val in temp[::-1]:
            self.res.append(val)

    def add_leafs(self, root):
        """Traverse all the leaf nodes"""
        if self.isLeaf(root):
            self.res.append(root.val)
            return

        if root.left:
            self.add_leafs(root.left)
        if root.right:
            self.add_leafs(root.right)

    def traverseBoundary(self, root):
        self.add_left_boundary(root)
        self.add_leafs(root)
        self.add_right_boundary(root)


sol = Solution()
sol.traverseBoundary(tree_root)
print(sol.res)
