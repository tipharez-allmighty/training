package heap

func getSum(slice []int) int {
	sum := 0
	for i := range slice {
		sum += slice[i]
	}
	return sum
}

func getIndex(slice []int, value int) int {
	for idx, val := range slice {
		if value == val {
			return idx
		}
	}
	return -1
}

func isPossible(target []int) bool {
	heap := MaxHeap{container: append([]int{}, target...)}
	heap.Heapify()
	totalSum := getSum(target)
	for {
		maxElement := heap.Pop()
		if maxElement == 1 {
			return true
		}
		sumOfOthers := totalSum - maxElement
		if sumOfOthers == 1 {
			return true
		}
		if sumOfOthers <= 0 || maxElement <= sumOfOthers {
			return false
		}
		newValue := maxElement % sumOfOthers
		if newValue <= 0 {
			return false
		}
		totalSum = sumOfOthers + newValue
		heap.Push(newValue)
	}
}
