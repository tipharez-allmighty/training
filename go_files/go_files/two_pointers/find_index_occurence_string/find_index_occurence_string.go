package main

import (
	"fmt"
)

func strStr(haystack string, needle string) int {
	if len(needle) == 0 {
		return 0
	}
	lps := make([]int, len(needle))
	prevLPS, i := 0, 1
	for i < len(needle) {
		if needle[prevLPS] == needle[i] {
			lps[i] = prevLPS + 1
			prevLPS++
			i++
		} else if prevLPS == 0 {
			prevLPS = 0
			lps[i] = 0
			i++
		} else {
			prevLPS = lps[prevLPS-1]
		}
	}
	j := 0
	k := 0
	for j < len(haystack) {
		if haystack[j] == needle[k] {
			j++
			k++
			if k == len(needle) {
				return j - k
			}
		} else if k == 0 {
			j++
		} else if k == len(needle) {
			return j - len(needle)
		} else {
			k = lps[k-1]
		}
	}
	return -1
}

func main() {
	fmt.Println(strStr("a", "a"))
}
