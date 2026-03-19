package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func averageOfLevels(root *TreeNode) []float64 {
	averages := []float64{}
	if root == nil {
		return averages
	}
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		levelSize := len(queue)
		levelSum := 0
		for i := 0; i < levelSize; i++ {
			currentNode := queue[0]
			queue = queue[1:]
			levelSum += currentNode.Val
			if currentNode.Left != nil {
				queue = append(queue, currentNode.Left)
			}
			if currentNode.Right != nil {
				queue = append(queue, currentNode.Right)
			}
		}
		averages = append(averages, float64(levelSum)/float64(levelSize))
	}
	return averages
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
		averageOfLevels(&rootNode),
	)
}
