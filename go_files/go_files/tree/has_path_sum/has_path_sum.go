package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func HasPathSum(root *TreeNode, targetSum int) bool {
	if root == nil {
		return false
	}
	if root.Left == nil && root.Right == nil {
		return root.Val == targetSum
	}
	newSum := targetSum - root.Val
	return HasPathSum(root.Left, newSum) || HasPathSum(root.Right, newSum)
}

type NodeSum struct {
	Node *TreeNode
	Sum  int
}

func HasPathSumStack(root *TreeNode, targetSum int) bool {
	if root == nil {
		return false
	}
	stack := []NodeSum{}
	stack = append(stack, NodeSum{
		Node: root,
		Sum:  root.Val,
	})

	for len(stack) > 0 {
		current := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if current.Node.Left == nil && current.Node.Right == nil {
			if current.Sum == targetSum {
				return true
			}
		}
		if current.Node.Left != nil {
			stack = append(stack, NodeSum{
				Node: current.Node.Left,
				Sum:  current.Node.Left.Val + current.Sum,
			})
		}
		if current.Node.Right != nil {
			stack = append(stack, NodeSum{
				Node: current.Node.Right,
				Sum:  current.Node.Right.Val + current.Sum,
			})
		}
	}
	return false
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
	fmt.Println(HasPathSumStack(&rootNode, 22))
}
