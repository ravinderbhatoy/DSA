from representation import TreeNode
from buildTree import build_tree


class NodeValue:
    def __init__(self, minvalue, maxvalue, maxsum, isBST):
        self.minvalue = minvalue
        self.maxvalue = maxvalue
        self.maxsum = maxsum
        self.isBST = isBST


def maxSumBST(root: TreeNode):
    ultimateSum = 0

    def largestBSTHelper(root: TreeNode):
        nonlocal ultimateSum
        if not root:
            return NodeValue(float('inf'), float('-inf'), 0, True)

        left = largestBSTHelper(root.left)
        right = largestBSTHelper(root.right)

        if ((left.isBST and left.maxvalue < root.val)
                and (right.isBST and root.val < right.minvalue)):
            currSum = left.maxsum + right.maxsum + root.val
            ultimateSum = max(ultimateSum, currSum)
            return NodeValue(min(root.val, left.minvalue),
                             max(root.val, right.maxvalue), currSum, True)

        return NodeValue(float('inf'), float('-inf'),
                         max(right.maxsum, left.maxsum), False)

    largestBSTHelper(root)
    return ultimateSum


root = build_tree([1, 4, 3, 2, 4, 2, 5, None, None,
                   None, None, None, None, 4, 6])

print(maxSumBST(root))
