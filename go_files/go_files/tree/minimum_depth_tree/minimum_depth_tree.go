package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func MinDepth(root *TreeNode) int {
	if root == nil {
		return 0
	} else if root.Left == nil {
		return 1 + MinDepth(root.Right)
	} else if root.Right == nil {
		return 1 + MinDepth(root.Left)
	} else {
		return 1 + min(MinDepth(root.Left), MinDepth(root.Right))
	}
}

func main() {
	treeNode3 := TreeNode{
		Val: 3,
	}
	treeNode4 := TreeNode{
		Val: 4,
	}
	treeNode5 := TreeNode{
		Val: 5,
	}
	treeNode2 := TreeNode{
		Val:   2,
		Left:  &treeNode4,
		Right: &treeNode5,
	}
	rootNode := TreeNode{
		Val:   1,
		Left:  &treeNode2,
		Right: &treeNode3,
	}
	fmt.Println(MinDepth(&rootNode))
}
