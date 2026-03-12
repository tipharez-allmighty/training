package main

import (
	"fmt"
)

func findErrorNums(nums []int) []int {
	counts := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		counts[nums[i]]++
	}
	for i := 1; i <= len(nums); i++ {
		if _, ok := counts[i]; !ok {
			counts[i] = 0
		}
	}
	duplicate_value := 0
	missing_value := 0
	for key, value := range counts {
		if value > 1 {
			duplicate_value = key
		}
		if value == 0 {
			missing_value = key
		}
	}
	return []int{duplicate_value, missing_value}
}

func main() {
	fmt.Println(findErrorNums([]int{1, 2, 2, 4}))
}
