package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	}
	if p == nil || q == nil {
		return false
	}
	if p.Val == q.Val {
		return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
	}
	return false
}

func main() {
	leftSubA := TreeNode{Val: 3}
	leftA := TreeNode{Val: 2, Left: &leftSubA}
	rightA := TreeNode{Val: 2, Right: nil}
	treeA := TreeNode{Val: 1, Left: &leftA, Right: &rightA}

	leftSubB := TreeNode{Val: 3}
	leftB := TreeNode{Val: 2, Left: &leftSubB}
	rightB := TreeNode{Val: 2, Right: nil}
	treeB := TreeNode{Val: 1, Left: &leftB, Right: &rightB}

	fmt.Println("Is Same Tree: ", isSameTree(&treeA, &treeB))
}
