package main

import "fmt"

func licenseKeyFormatting(s string, k int) string {
	var result []byte
	count := 0
	for i := len(s) - 1; i >= 0; i-- {
		if s[i] == '-' {
			continue
		}
		var upperCaseLetter byte
		if s[i] >= 'a' && s[i] <= 'z' {
			upperCaseLetter = s[i] - 32
		} else {
			upperCaseLetter = s[i]
		}
		if count == k {
			result = append(result, []byte{'-', upperCaseLetter}...)
			count = 1
		} else {
			result = append(result, upperCaseLetter)
			count++
		}
	}
	left, right := 0, len(result)-1
	for left < right {
		result[left], result[right] = result[right], result[left]
		left++
		right--
	}
	return string(result)
}

func main() {
	fmt.Println(licenseKeyFormatting("5F3Z-2e-9-w", 4))
	fmt.Println(licenseKeyFormatting("2-5g-3J", 2))
	fmt.Println(licenseKeyFormatting("---", 3))
}
