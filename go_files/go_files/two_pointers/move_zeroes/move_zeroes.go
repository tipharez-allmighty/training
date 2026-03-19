package main

import (
	"fmt"
)

func moveZeroes(nums []int) {
	j := 0

	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			nums[j], nums[i] = nums[i], nums[j]
			j++
		}
	}
}

func main() {
	nums := []int{1, 2, 0, 3, 12}
	moveZeroes(nums)
	fmt.Println(nums)
}
