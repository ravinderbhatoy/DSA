from representation import TreeNode
from inOrderIterative import inOrderTraversal


def changeTree(root: TreeNode | None):
    if root is None:
        return

    child = 0

    if root.left:
        child += root.left.val
    if root.right:
        child += root.right.val

    if child >= root.val:
        root.val = child
    else:
        if root.left:
            root.left.val = root.val
        if root.right:
            root.right.val = root.val

    changeTree(root.left)
    changeTree(root.right)

    sm = 0
    if root.left:
        sm += root.left.val
    if root.right:
        sm += root.right.val

    if root.left or root.right:
        root.val = sm


root = TreeNode(2)
root.left = TreeNode(35)
root.left.right = TreeNode(3)
root.left.left = TreeNode(2)
root.right = TreeNode(10)
root.right.left = TreeNode(2)
root.right.right = TreeNode(5)

changeTree(root)
print(inOrderTraversal(root))
