package main

import (
	"fmt"
)

func removeElement(nums []int, val int) int {
	p1 := 0
	p2 := len(nums) - 1

	for p1 <= p2 {
		if nums[p1] != val && nums[p2] == val {
			p1 += 1
			p2 -= 1
		} else if nums[p2] != val && nums[p1] == val {
			nums[p1] = nums[p2]
			p1 += 1
			p2 -= 1
		} else if nums[p1] != val && nums[p2] != val {
			p1 += 1
		} else if nums[p1] == val && nums[p2] == val {
			p2 -= 1
		}
	}
	return p1
}

func main() {
	nums := []int{3, 2, 2, 2, 3}
	fmt.Println(removeElement(nums, 3))
}
