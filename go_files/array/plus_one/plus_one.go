package main

import "fmt"

func plusOne(digits []int) []int {
	carry := false
	for i := len(digits) - 1; i >= 0; i-- {
		currentDigit := digits[i]
		switch {
		case currentDigit < 9:
			digits[i]++
			carry = false
			return digits
		case currentDigit == 9:
			digits[i] = 0
			carry = true
		}
		if i == 0 && digits[i] == 0 && carry == true {
			newArray := []int{1}
			newArray = append(newArray, digits...)
			return newArray
		}
	}
	return digits
}

func betterPlusOne(digits []int) []int {
	for i := len(digits) - 1; i >= 0; i-- {

		if digits[i] < 9 {
			digits[i]++
			return digits
		}

		digits[i] = 0
	}

	return append([]int{1}, digits...)
}

func main() {
	fmt.Println(betterPlusOne([]int{1, 2, 3}))
}
