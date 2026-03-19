package main

import (
	"fmt"
	"regexp"
	"strings"
)

func isPalindrome(s string) bool {
	reg := regexp.MustCompile("[^a-zA-Z0-9]+")
	lower_string := strings.ToLower(s)
	clean_string := reg.ReplaceAllString(lower_string, "")

	p1 := 0
	p2 := len(clean_string) - 1

	for p1 <= p2 {
		if clean_string[p1] != clean_string[p2] {
			return false
		}
		p1++
		p2--
	}
	return true
}

func main() {
	fmt.Println(isPalindrome("A man, a plan, a canal: Panama"))
}
