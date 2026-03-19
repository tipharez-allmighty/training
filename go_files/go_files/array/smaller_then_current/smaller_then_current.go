package main

import (
	"fmt"
)

func smallerNumbersThanCurrent(nums []int) []int {
	result := make([]int, len(nums))
	for i := 0; i < len(nums); i++ {
		targetNum := nums[i]
		for _, num := range nums {
			if targetNum > num {
				result[i]++
			}
		}
	}
	return result
}

func main() {
	fmt.Println(smallerNumbersThanCurrent([]int{8, 1, 2, 2, 3}))
}
