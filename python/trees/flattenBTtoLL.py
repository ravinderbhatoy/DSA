from representation import TreeNode
from morisTraversal import inorder
from buildTree import build_tree


def flatterBTtoLL(root: TreeNode) -> None:
    prev = None

    def flatten(node: TreeNode) -> None:
        nonlocal prev
        if node is None:
            return

        flatten(node.right)
        flatten(node.left)

        node.right = prev
        node.left = None
        prev = node

    def morisPreorder(root: TreeNode) -> list[int] | None:
        curr = root
        while curr:
            if curr.left:
                prev = curr.left

                while prev.right:
                    prev = prev.right

                prev.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right

    morisPreorder(root)


root = build_tree([1, 2, 5, 3, 4, None, 6])
flatterBTtoLL(root)
print(inorder(root))
