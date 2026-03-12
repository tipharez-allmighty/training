package main

import (
	"fmt"
)

func findDisappearedNumbers(nums []int) []int {
	numMap := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		numMap[i+1] = 0
	}
	for _, num := range nums {
		if _, ok := numMap[num]; ok {
			numMap[num]++
		}
	}
	result := []int{}
	for key, value := range numMap {
		if value == 0 {
			result = append(result, key)
		}
	}
	return result
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func findDisappearedNumbersInPlace(nums []int) []int {
	for _, num := range nums {
		i := int(abs(num)) - 1
		nums[i] = -1 * abs(nums[i])
	}
	result := []int{}
	for i, num := range nums {
		if num > 0 {
			result = append(result, i+1)
		}
	}
	return result
}

func main() {
	fmt.Println(findDisappearedNumbersInPlace([]int{4, 3, 2, 7, 8, 2, 3, 1}))
}
