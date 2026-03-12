package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func traverseTreeInOrder(root *TreeNode, orderedNodes *[]int) *TreeNode {
	if root != nil {
		traverseTreeInOrder(root.Left, orderedNodes)
		*orderedNodes = append(*orderedNodes, root.Val)
		traverseTreeInOrder(root.Right, orderedNodes)
	}
	return root
}

func inOrderTraversal(root *TreeNode) []int {
	orderedNodes := make([]int, 0)
	traverseTreeInOrder(root, &orderedNodes)
	return orderedNodes
}

func traverseTreePreOrder(root *TreeNode, orderedNodes *[]int) *TreeNode {
	if root != nil {
		*orderedNodes = append(*orderedNodes, root.Val)
		traverseTreePreOrder(root.Left, orderedNodes)
		traverseTreePreOrder(root.Right, orderedNodes)
	}
	return root
}

func preorderTraversal(root *TreeNode) []int {
	orderedNodes := make([]int, 0)
	traverseTreePreOrder(root, &orderedNodes)
	return orderedNodes
}

func traverseTreePostOrder(root *TreeNode, orderedNodes *[]int) *TreeNode {
	if root != nil {
		traverseTreePostOrder(root.Left, orderedNodes)
		traverseTreePostOrder(root.Right, orderedNodes)
		*orderedNodes = append(*orderedNodes, root.Val)
	}
	return root
}

func postorderTraversal(root *TreeNode) []int {
	orderedNodes := make([]int, 0)
	traverseTreePostOrder(root, &orderedNodes)
	return orderedNodes
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
	fmt.Println(
		"Traversed Tree In Order: ", inOrderTraversal(&rootNode),
	)
}
