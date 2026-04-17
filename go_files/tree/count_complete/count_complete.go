package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func countNodesOne(root *TreeNode) int {
	sum := 1
	countResult(root, &sum)
	return sum
}

func countResult(root *TreeNode, sum *int) {
	if root == nil {
		*sum = 0
		return
	}
	if root.Left != nil {
		*sum++
		countResult(root.Left, sum)
	}
	if root.Right != nil {
		*sum++
		countResult(root.Right, sum)
	}
}

func countNodes(root *TreeNode) int {
	if root == nil {
		return 0
	}
	left := root
	leftHeight := 0
	for left != nil {
		left = left.Left
		leftHeight++
	}
	right := root
	rightHeight := 0
	for right != nil {
		right = right.Right
		rightHeight++
	}
	if leftHeight == rightHeight {
		return (1 << leftHeight) - 1
	}
	return 1 + countNodes(root.Left) + countNodes(root.Right)
}

func main() {
	n7 := &TreeNode{Val: 7}
	n6 := &TreeNode{Val: 6}
	n5 := &TreeNode{Val: 5}
	n4 := &TreeNode{Val: 4}
	n3 := &TreeNode{Val: 3, Left: n6, Right: n7}
	n2 := &TreeNode{Val: 2, Left: n4, Right: n5}
	rootNode := &TreeNode{Val: 2, Left: n2, Right: n3}
	fmt.Println(countNodes(rootNode))
}
