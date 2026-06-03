// Package heap implements heap for leetcode tasks to use
package heap

type MaxHeap struct {
	container []int
}

func (h *MaxHeap) Len() int {
	return len(h.container)
}

func (h *MaxHeap) Push(element int) {
	h.container = append(h.container, element)
	h.bubbleUp()
}

func (h *MaxHeap) Pop() int {
	h.swap(0, h.Len()-1)
	maxValue := h.container[h.Len()-1]
	h.container = h.container[:h.Len()-1]
	h.bubbleDown(h.Len(), 0)
	return maxValue
}

func (h *MaxHeap) Heapify() {
	n := h.Len()
	i := n/2 - 1
	for j := i; j >= 0; j-- {
		h.bubbleDown(n, j)
	}
}

func (h *MaxHeap) swap(i, j int) {
	h.container[i], h.container[j] = h.container[j], h.container[i]
}

func (h *MaxHeap) bubbleDown(n, i int) {
	parent := i
	left := 2*i + 1
	right := 2*i + 2
	if left < n && h.container[parent] < h.container[left] {
		parent = left
	}
	if right < n && h.container[parent] < h.container[right] {
		parent = right
	}
	if parent != i {
		h.swap(parent, i)
		h.bubbleDown(n, parent)
	}
}

func (h *MaxHeap) bubbleUp() {
	i := h.Len() - 1
	parent := (i - 1) / 2
	for i != 0 && h.container[i] > h.container[parent] {
		h.swap(i, parent)
		i = parent
		parent = (i - 1) / 2
	}
}

type MinHeap struct {
	container []int
}

func (h *MinHeap) Len() int {
	return len(h.container)
}

func (h *MinHeap) Push(element int) {
	h.container = append(h.container, element)
	h.bubbleUp()
}

func (h *MinHeap) Pop() int {
	h.swap(0, h.Len()-1)
	maxValue := h.container[h.Len()-1]
	h.container = h.container[:h.Len()-1]
	h.bubbleDown(h.Len(), 0)
	return maxValue
}

func (h *MinHeap) Heapify() {
	n := h.Len()
	i := n/2 - 1
	for j := i; j >= 0; j-- {
		h.bubbleDown(n, j)
	}
}

func (h *MinHeap) swap(i, j int) {
	h.container[i], h.container[j] = h.container[j], h.container[i]
}

func (h *MinHeap) bubbleDown(n, i int) {
	parent := i
	left := 2*i + 1
	right := 2*i + 2
	if left < n && h.container[parent] > h.container[left] {
		parent = left
	}
	if right < n && h.container[parent] > h.container[right] {
		parent = right
	}
	if parent != i {
		h.swap(parent, i)
		h.bubbleDown(n, parent)
	}
}

func (h *MinHeap) bubbleUp() {
	i := h.Len() - 1
	parent := (i - 1) / 2
	for i != 0 && h.container[i] < h.container[parent] {
		h.swap(i, parent)
		i = parent
		parent = (i - 1) / 2
	}
}
