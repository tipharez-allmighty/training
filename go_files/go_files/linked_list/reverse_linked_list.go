package main

import (
	"fmt"
)

type Node struct {
	Value int
	Next  *Node
}

func (node *Node) String() string {
	if node == nil {
		return "nil"
	}
	return fmt.Sprintf("{Value: %d, Next: %v}", node.Value, node.Next)
}

func reverseList(node *Node) *Node {
	var prevNode *Node = nil
	currentNode := node
	for currentNode != nil {
		tempNode := &Node{
			Value: currentNode.Value,
			Next:  prevNode,
		}
		prevNode = tempNode
		currentNode = currentNode.Next
	}
	return prevNode
}

func main() {
	node1 := Node{Value: 1}
	node2 := Node{Value: 2}
	node3 := Node{Value: 3}
	node4 := Node{Value: 4}
	node1.Next = &node2
	node1.Next.Next = &node3
	node1.Next.Next.Next = &node4
	reversedListValue := reverseList(&node1)
	fmt.Println(reversedListValue)
	fmt.Println(&node1)
}
