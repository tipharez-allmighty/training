package main

import (
	"fmt"
)

func merge(nums1 []int, m int, nums2 []int, n int) {
	i := len(nums1) - 1
	j := m - 1
	k := n - 1
	for j >= 0 && k >= 0 {
		if nums2[k] > nums1[j] {
			nums1[i] = nums2[k]
			k--
		} else if nums1[j] >= nums2[k] {
			nums1[i] = nums1[j]
			j--
		}
		i--
	}
	for k >= 0 {
		nums1[i] = nums2[k]
		k--
		i--
	}
}

func main() {
	nums1 := []int{0}
	m := 0
	nums2 := []int{1}
	n := 1
	merge(nums1, m, nums2, n)
	fmt.Println(nums1)
}
