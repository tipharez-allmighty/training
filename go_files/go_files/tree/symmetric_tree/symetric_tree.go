package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}
	return isMirror(root.Left, root.Right)
}

func isMirror(rootOne *TreeNode, rootTwo *TreeNode) bool {
	if rootOne == nil && rootTwo == nil {
		return true
	}
	if rootOne == nil || rootTwo == nil {
		return false
	}
	if rootOne.Val != rootTwo.Val {
		return false
	}
	return isMirror(rootOne.Left, rootTwo.Right) && isMirror(rootTwo.Left, rootOne.Right)
}

func main() {
	leftSubChild := TreeNode{Val: 3}
	leftBranch := TreeNode{
		Val:  2,
		Left: &leftSubChild,
	}

	rightBranch := TreeNode{
		Val:   2,
		Right: nil,
	}

	rootNode := TreeNode{
		Val:   1,
		Left:  &leftBranch,
		Right: &rightBranch,
	}

	fmt.Println("Is Tree Symmetric: ", isSymmetric(&rootNode))
}
