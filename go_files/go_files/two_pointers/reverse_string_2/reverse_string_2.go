package main

import (
	"fmt"
)

func reverseString(s string, k int) string {
	bytes := []byte(s)
	for i := 0; i < len(bytes); i += k * 2 {
		p1 := i
		p2 := min(i+k-1, len(bytes)-1)
		for p1 < p2 {
			bytes[p1], bytes[p2] = bytes[p2], bytes[p1]
			p1++
			p2--
		}
	}
	return string(bytes)
}

func main() {
	s := "a"
	k := 2

	fmt.Println(reverseString(s, k))
}
