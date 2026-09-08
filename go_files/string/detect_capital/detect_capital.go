package main

import (
	"unicode"
)

func detectCapitalUse(word string) bool {
	left := 0
	right := len(word) - 1
	patterns := map[int]bool{
		1: false,
		2: false,
		3: false,
	}
	if unicode.IsUpper(rune(word[left])) && unicode.IsLower(rune(word[right])) {
		patterns[1] = true
	} else if unicode.IsUpper(rune(word[left])) && unicode.IsUpper(rune(word[right])) {
		patterns[2] = true
	} else if unicode.IsLower(rune(word[left])) && unicode.IsLower(rune(word[right])) {
		patterns[3] = true
	} else {
		return false
	}
	left++
	right--
	for left <= right {
		if patterns[1] || patterns[3] {
			if unicode.IsUpper(rune(word[left])) || unicode.IsUpper(rune(word[right])) {
				return false
			}
		}
		if patterns[2] {
			if unicode.IsLower(rune(word[left])) || unicode.IsLower(rune(word[right])) {
				return false
			}
		}
		left++
		right--
	}
	return true
}

func detectCapitalUseOptimal(word string) bool {
	left := 0
	right := len(word) - 1
	var capitals int
	for left < right {
		if unicode.IsUpper(rune(word[left])) {
			capitals++
		}
		if unicode.IsUpper(rune(word[right])) {
			capitals++
		}
		left++
		right--
	}
	if left == right && unicode.IsUpper(rune(word[left])) {
		capitals++
	}
	if capitals == len(word) {
		return true
	}
	if capitals == 0 {
		return true
	}
	if capitals == 1 && unicode.IsUpper(rune(word[0])) {
		return true
	}

	return false
}

func detectCapitalUseEvenMoreOptimal(word string) bool {
	var capitals int
	for i := 0; i < len(word); i++ {
		if word[i] >= 'A' && word[i] <= 'Z' {
			capitals++
		}
	}
	return capitals == len(word) || capitals == 0 || (capitals == 1 && word[0] >= 'A' && word[0] <= 'Z')
}
