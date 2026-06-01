from representation import TreeNode


def bstFromPreorder(preorder: list[int]) -> TreeNode:
    # bst's inorder is sorted array just sort preorder to get
    # inorder

    inorder = sorted(preorder)

    inMap = {value: i for i, value in enumerate(inorder)}

    preIdx = 0

    def generate(inStart, inEnd):
        nonlocal preIdx
        if inStart > inEnd:
            return None

        val = preorder[preIdx]
        root = TreeNode(val)

        preIdx += 1

        index = inMap[val]
        root.left = generate(inStart, index - 1)
        root.right = generate(index + 1, inEnd)

        return root

    root = generate(0, len(inorder) - 1)
    return root


preorder = [8, 5, 1, 7, 10, 12]
print(bstFromPreorder(preorder))
