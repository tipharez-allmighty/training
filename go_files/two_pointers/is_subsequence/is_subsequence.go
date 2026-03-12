package main

import "fmt"

func isSubsequence(s string, t string) bool {
	p1 := 0
	p2 := 0
	for p1 < len(s) && p2 < len(t) {
		if s[p1] == t[p2] {
			p1++
		}
		if p1 == len(s) {
			return true
		}
		p2++
	}
	return p1 == len(s)
}

func main() {
	s := ""
	t := "ahbgdc"
	fmt.Println(isSubsequence(s, t))
}
