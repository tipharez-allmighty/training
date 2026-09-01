package stream_processing

import "sort"

type KthLargest struct {
	k    int
	nums []int
}

func Constructor(k int, nums []int) KthLargest {
	sort.Ints(nums)
	return KthLargest{k: k, nums: nums}
}

func (this *KthLargest) Add(val int) int {
	slow, fast := 0, 1
	if len(this.nums) == 0 {
		this.nums = []int{val}
	} else if this.nums[0] > val {
		this.nums = append([]int{val}, this.nums...)
	} else if this.nums[len(this.nums)-1] < val {
		this.nums = append(this.nums, val)
	} else {
		for fast < len(this.nums) {
			if this.nums[slow] <= val && this.nums[fast] >= val {
				this.nums = append(this.nums[:slow+1], append([]int{val}, this.nums[fast:]...)...)
				break
			}

			slow++
			fast++
		}
	}
	kthVal := 0
	if len(this.nums) < this.k {
		kthVal = this.nums[len(this.nums)-1]
	} else {
		kthVal = this.nums[len(this.nums)-this.k]
	}
	return kthVal
}
