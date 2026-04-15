package main

import "fmt"

func finalPrices(prices []int) []int {
	result := append([]int{}, prices...)
	stack := []int{}
	for idx, val := range prices {
		for len(stack) > 0 && prices[stack[len(stack)-1]] >= val {
			currentIdx := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			result[currentIdx] -= val
		}
		stack = append(stack, idx)
	}
	return result
}

func main() {
	prices := []int{8, 4, 6, 2, 3}
	fmt.Println(finalPrices(prices))
}
