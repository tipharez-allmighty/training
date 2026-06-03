package heap

type Coordinates struct {
	Sum int
	Row int
	Col int
}

type MinHeapCoordinates struct {
	container []Coordinates
}

func (h *MinHeapCoordinates) Len() int {
	return len(h.container)
}

func (h *MinHeapCoordinates) Push(node Coordinates) {
	h.container = append(h.container, node)
	h.bubbleUp()
}

func (h *MinHeapCoordinates) Pop() Coordinates {
	h.swap(0, h.Len()-1)

	minValue := h.container[h.Len()-1]
	h.container = h.container[:h.Len()-1]

	h.bubbleDown(h.Len(), 0)
	return minValue
}

func (h *MinHeapCoordinates) Heapify() {
	n := h.Len()
	i := n/2 - 1

	for j := i; j >= 0; j-- {
		h.bubbleDown(n, j)
	}
}

func (h *MinHeapCoordinates) swap(i, j int) {
	h.container[i], h.container[j] = h.container[j], h.container[i]
}

func (h *MinHeapCoordinates) bubbleDown(n, i int) {
	parent := i
	left := 2*i + 1
	right := 2*i + 2

	if left < n && h.container[parent].Sum > h.container[left].Sum {
		parent = left
	}

	if right < n && h.container[parent].Sum > h.container[right].Sum {
		parent = right
	}

	if parent != i {
		h.swap(parent, i)
		h.bubbleDown(n, parent)
	}
}

func (h *MinHeapCoordinates) bubbleUp() {
	i := h.Len() - 1
	parent := (i - 1) / 2

	for i != 0 && h.container[i].Sum < h.container[parent].Sum {
		h.swap(i, parent)
		i = parent
		parent = (i - 1) / 2
	}
}

func kSmallestPairs(nums1, nums2 []int, k int) [][]int {
	heap := MinHeapCoordinates{}
	visited := make(map[Coordinates]struct{})
	candidateSum := nums1[0] + nums2[0]
	currentCoordinates := Coordinates{Sum: candidateSum, Row: 0, Col: 0}
	heap.Push(currentCoordinates)
	visited[currentCoordinates] = struct{}{}
	var result [][]int
	for heap.Len() > 0 && k > 0 {
		currentMin := heap.Pop()
		k -= 1
		result = append(result, []int{nums1[currentMin.Row], nums2[currentMin.Col]})
		i := currentMin.Row + 1
		j := currentMin.Col + 1
		if i < len(nums1) {
			candidateSum = nums1[i] + nums2[currentMin.Col]
			currentCoordinates = Coordinates{Sum: candidateSum, Row: i, Col: currentMin.Col}
			if _, ok := visited[currentCoordinates]; !ok {
				heap.Push(currentCoordinates)
				visited[currentCoordinates] = struct{}{}
			}
		}
		if j < len(nums2) {
			candidateSum = nums1[currentMin.Row] + nums2[j]
			currentCoordinates = Coordinates{Sum: candidateSum, Row: currentMin.Row, Col: j}
			if _, ok := visited[currentCoordinates]; !ok {
				heap.Push(currentCoordinates)
				visited[currentCoordinates] = struct{}{}
			}
		}
	}
	return result
}
