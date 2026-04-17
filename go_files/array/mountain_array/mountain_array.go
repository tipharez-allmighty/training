package main

import "fmt"

func validMountainArray(arr []int) bool {
	i := 0
	for i < len(arr)-1 && arr[i] < arr[i+1] {
		i++
	}
	peak := i
	if peak == 0 || peak == len(arr)-1 {
		return false
	}
	for i < len(arr)-1 && arr[i+1] < arr[i] {
		i++
	}
	if i == len(arr)-1 {
		return true
	} else {
		return false
	}
}

func main() {
	fmt.Println(validMountainArray([]int{0, 3, 2, 1}))
}
