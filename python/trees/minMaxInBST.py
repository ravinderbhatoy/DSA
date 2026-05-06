from representation import bst_root


def findMax(root):
    while root and root.right:
        root = root.right
    return root.val if root else root


def findMin(root):
    while root and root.left:
        root = root.left
    return root.val if root else root


print(findMax(bst_root))
print(findMin(bst_root))
