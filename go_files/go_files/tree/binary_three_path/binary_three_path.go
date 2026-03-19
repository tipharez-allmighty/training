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

func binaryTreePaths(root *TreeNode) []string {
	path := []string{}
	findPath(root, &path, "")
	return path
}

func findPath(root *TreeNode, path *[]string, currentPath string) {
	if root != nil {
		if len(currentPath) > 0 {
			currentPath += "->"
		}
		currentPath += fmt.Sprint(root.Val)
		if root.Left == nil && root.Right == nil {
			*path = append(*path, currentPath)
		}
		if root.Left != nil {
			findPath(root.Left, path, currentPath)
		}
		if root.Right != nil {
			findPath(root.Right, path, currentPath)
		}
	}
}

func binaryTreePathsSlice(root *TreeNode) []string {
	path := []string{}
	stack := []string{}
	findPathSlice(root, &path, &stack)
	return path
}

func findPathSlice(root *TreeNode, path *[]string, stack *[]string) {
	if root != nil {
		*stack = append(*stack, strconv.Itoa(root.Val))
		if root.Left == nil && root.Right == nil {
			*path = append(*path, strings.Join(*stack, "->"))
		}
		if root.Left != nil {
			findPathSlice(root.Left, path, stack)
		}
		if root.Right != nil {
			findPathSlice(root.Right, path, stack)
		}
		*stack = (*stack)[:len(*stack)-1]
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
	fmt.Println(
		binaryTreePaths(&rootNode),
	)
}
