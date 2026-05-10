package dsa

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}


root := TreeNode{Val: 10}
root.Left = &TreeNode{Val: 20}
root.Right = &TreeNode{Val: 20}

func distanceK(root *TreeNode, target *TreeNode, k int) []int {
	res := make([]int, 0)

	source := func findNode(root* TreeNode, target *TreeNode) *TreeNode {
		queue := make([]int)

	}
	return res
}


