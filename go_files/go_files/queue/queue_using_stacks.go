package main

type QueueStacks struct {
	stackIn, stackOut []int
}

func Constructor() QueueStacks {
	return QueueStacks{
		stackIn:  make([]int, 0),
		stackOut: make([]int, 0),
	}
}

func (this *QueueStacks) Push(x int) {
	this.stackIn = append(this.stackIn, x)
}

func (this *QueueStacks) Pop() int {
	if this.Empty() {
		panic("Queue is empty")
	}
	var topValue int
	if len(this.stackOut) == 0 {
		this.Move()
	}
	topValue = this.stackOut[len(this.stackOut)-1]
	this.stackOut = this.stackOut[:len(this.stackOut)-1]
	return topValue
}

func (this *QueueStacks) Move() {
	for i := len(this.stackIn) - 1; i >= 0; i-- {
		this.stackOut = append(this.stackOut, this.stackIn[i])
		this.stackIn = this.stackIn[:i]
	}
}

func (this *QueueStacks) Peek() int {
	if this.Empty() {
		panic("Queue is empty")
	}
	if len(this.stackOut) == 0 {
		this.Move()
	}
	return this.stackOut[len(this.stackOut)-1]
}

func (this *QueueStacks) Empty() bool {
	if len(this.stackIn) == 0 && len(this.stackOut) == 0 {
		return true
	}
	return false
}
