package heap

func lastStoneWeight(stones []int) int {
	heap := Heap{container: stones}
	heap.Heapify()
	for heap.Len() > 1 {
		firstLargestStone, secondLargestStone := heap.Pop(), heap.Pop()
		if firstLargestStone != secondLargestStone {
			heap.Push(firstLargestStone - secondLargestStone)
		}
	}
	if heap.Len() == 0 {
		return 0
	}
	return heap.Pop()
}
