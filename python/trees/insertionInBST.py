from representation import bst_root, TreeNode
from inOrderIterative import inOrderTraversal


def insertIntoBST(root: TreeNode, val: int):

    if not root:
        return TreeNode(val)

    curr = root
    newNode = TreeNode(val)
    parent = None

    while curr:
        parent = curr
        if curr.val <= val:
            curr = curr.right
        else:
            curr = curr.left

    if parent.val < val:
        parent.right = newNode
    else:
        parent.left = newNode

    return root


root = insertIntoBST(bst_root, 3)
print(inOrderTraversal(root))
