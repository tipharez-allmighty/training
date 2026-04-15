package main

import "fmt"

func dailyTemperatures(temperatures []int) []int {
	result := make([]int, len(temperatures))
	stack := []int{}
	for idx, val := range temperatures {
		for len(stack) > 0 && val > temperatures[stack[len(stack)-1]] {
			currentIdx := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			result[currentIdx] = idx - currentIdx
		}
		stack = append(stack, idx)
	}
	return result
}

func main() {
	temperatures := []int{73, 74, 75, 71, 69, 72, 76, 73}
	fmt.Println(dailyTemperatures(temperatures))
}
