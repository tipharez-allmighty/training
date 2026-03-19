package main

import (
	"fmt"
)

func buildArray(target []int, n int) []string {
	output := []string{}
	i := 1
	j := 0
	for i <= n && j < len(target) {
		output = append(output, "Push")
		if target[j] != i {
			output = append(output, "Pop")
		} else {
			j++
		}
		i++
	}
	return output
}

func main() {
	target := []int{1, 3}
	n := 4
	array := buildArray(target, n)
	fmt.Println(array)
}
