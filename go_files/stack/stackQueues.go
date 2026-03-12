package main

import "errors"

var ErrorEmptyStack = errors.New("Stack is Empty")

type MyStack struct {
	queue_one, queue_two []int
}

func Constructor() MyStack {
	return MyStack{
		queue_one: make([]int, 0),
		queue_two: make([]int, 0),
	}
}

func (this *MyStack) Push(x int) {
	if len(this.queue_one) == 0 {
		this.queue_one = append(this.queue_one, x)
	} else {
		this.Swap()
		this.queue_one = append(this.queue_one, x)
		this.Move()
	}
}

func (this *MyStack) Pop() (int, error) {
	if this.Empty() {
		return 0, ErrorEmptyStack
	}
	value_to_return := this.queue_one[0]
	this.queue_one = this.queue_one[1:]
	return value_to_return, nil
}

func (this *MyStack) Top() (int, error) {
	if !this.Empty() {
		return this.queue_one[0], nil
	}
	return 0, ErrorEmptyStack
}

func (this *MyStack) Empty() bool {
	return len(this.queue_one) == 0
}

func (this *MyStack) Swap() {
	this.queue_one, this.queue_two = this.queue_two, this.queue_one
}

func (this *MyStack) Move() {
	for len(this.queue_two) != 0 {
		this.queue_one = append(this.queue_one, this.queue_two[0])
		this.queue_two = this.queue_two[1:]
	}
}
