package main

import "fmt"

func main() {
	x := 10
	queueStack := Constructor()
	for i := 0; i <= x; i++ {
		queueStack.Push(i)
	}
	value := queueStack.Pop()
	peek := queueStack.Peek()
	fmt.Println("Popped value: ", value, "Peek value: ", peek, "StackIn: ", queueStack.stackIn, "StackOut: ", queueStack.stackOut)

}
