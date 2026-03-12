package main

import (
	"fmt"
)

func factorial(n int) int {
	if n == 0 {
		return 1
	}
	if n <= 2 {
		return n
	}
	return n * (factorial(n - 1))
}

func fib(n int) int {
	if n < 2 {
		return n
	}
	return fib(n-2) + fib(n-1)
}

func fibTab(n int) int {
	if n == 0 {
		return n
	}
	tab := []int{0, 1}
	for i := 2; i < n+1; i++ {
		tab = append(tab, tab[i-1]+tab[i-2])
	}
	return tab[n]
}

func twoSum(nums []int, target int) []int {
	seen := make(map[int]int)

	for idx, value := range nums {
		complement := target - value
		if _, ok := seen[complement]; ok {
			return []int{seen[complement], idx}
		}
		seen[value] = idx
	}
	return nil
}

func bubbleSort(nums []int) {
	for i := range nums[:len(nums)-1] {
		for j := range nums[:len(nums)-i-1] {
			if nums[j] > nums[j+1] {
				nums[j], nums[j+1] = nums[j+1], nums[j]
			}
		}
	}
}

func main() {
	someArray := []int{7, 15, 11, 2}
	fmt.Println(factorial(10))
	fmt.Println(fib(10))
	fmt.Println(fibTab(10))
	fmt.Println(twoSum(someArray, 9))
	bubbleSort(someArray)
	fmt.Println(someArray)

}
