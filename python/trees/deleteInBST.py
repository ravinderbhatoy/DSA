from representation import bst_root, TreeNode
from inOrderIterative import inOrderTraversal
from preOrderIterative import pre_order_traverse
from buildTree import build_tree


def deleteNode(root: TreeNode, val: int):
    if not root:
        return root

    if root.val < val:
        root.right = deleteNode(root.right, val)
    elif root.val > val:
        root.left = deleteNode(root.left, val)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
    return root


root = build_tree([5, 3, 6, 2, 4, None, 7])
root = deleteNode(root, 7)
print("INORDER:", inOrderTraversal(root))
print("PREORDER:", pre_order_traverse(root))
