package main

import (
	"fmt"
	"strconv"
	"strings"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sumRootToLeaf(root *TreeNode) int {
	pathsSum := 0
	stack := []string{}
	findPathSums(root, &pathsSum, &stack)
	return pathsSum
}

func findPathSums(root *TreeNode, pathsSum *int, stack *[]string) {
	if root != nil {
		*stack = append(*stack, strconv.Itoa(root.Val))
		if root.Left == nil && root.Right == nil {
			binary := strings.Join(*stack, "")
			number, err := strconv.ParseInt(binary, 2, 64)
			if err != nil {
				panic(err)
			}
			*pathsSum += int(number)
		}
		if root.Left != nil {
			findPathSums(root.Left, pathsSum, stack)
		}
		if root.Right != nil {
			findPathSums(root.Right, pathsSum, stack)
		}
		*stack = (*stack)[:len(*stack)-1]
	}
}

func main() {
	treeNode3 := TreeNode{
		Val: 1,
	}
	treeNode4 := TreeNode{
		Val: 0,
	}
	treeNode5 := TreeNode{
		Val: 1,
	}
	treeNode2 := TreeNode{
		Val:   1,
		Left:  &treeNode4,
		Right: &treeNode5,
	}
	rootNode := TreeNode{
		Val:   0,
		Left:  &treeNode2,
		Right: &treeNode3,
	}
	fmt.Println(
		sumRootToLeaf(&rootNode),
	)
}
