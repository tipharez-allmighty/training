package main

import (
	"fmt"
)

func reverseString(s []byte) {
	p1 := 0
	p2 := len(s) - 1

	for p1 < p2 {
		s[p1], s[p2] = s[p2], s[p1]
		p1 += 1
		p2 -= 1
	}
}

func main() {
	s := []byte{'h', 'e', 'l', 'l', 'o'}
	reverseString(s)
	fmt.Println(s)
}
