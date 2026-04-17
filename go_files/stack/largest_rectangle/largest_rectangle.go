package main

import "fmt"

func largestRectangleArea(heights []int) int {
	maxArea := 0
	stack := []int{}
	heights = append(heights, 0)
	for idx := range heights {
		for len(stack) > 0 && heights[idx] < heights[stack[len(stack)-1]] {
			currentIdx := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			var width int
			if len(stack) == 0 {
				width = idx
			} else {
				width = idx - stack[len(stack)-1] - 1
			}
			area := heights[currentIdx] * (width)
			maxArea = max(maxArea, area)
		}
		stack = append(stack, idx)
	}
	return maxArea
}

func main() {
	heights := []int{2, 1, 5, 6, 2, 3}
	fmt.Println(largestRectangleArea(heights))
}
