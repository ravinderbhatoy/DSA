class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree_root = TreeNode(1)
tree_root.left = TreeNode(2)
tree_root.right = TreeNode(3)
tree_root.left.left = TreeNode(4)
tree_root.left.right = TreeNode(5)
tree_root.right.right = TreeNode(7)
tree_root.right.left = TreeNode(6)


# Binary Search Tree

bst_root = TreeNode(8)

bst_root.left = TreeNode(5)
bst_root.left.left = TreeNode(4)
bst_root.left.right = TreeNode(7)
bst_root.left.right.left = TreeNode(6)

bst_root.right = TreeNode(12)
bst_root.right.left = TreeNode(10)
bst_root.right.right = TreeNode(14)
bst_root.right.right.left = TreeNode(13)


# if __name__ == "__main__":
#     """
#                   1
#                  / \
#                 2   3
#                / \ / \
#               4  5 6  7
#     """
