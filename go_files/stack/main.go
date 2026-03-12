package main

import "fmt"

func main() {
	stack := Constructor()
	for i := 0; i <= 10; i++ {
		stack.Push(i)
	}
	fmt.Println(stack)
	stack.Pop()
	stack.Pop()
	fmt.Println(stack.queue_one)
}
