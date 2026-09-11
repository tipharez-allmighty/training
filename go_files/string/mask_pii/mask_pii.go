package main

import "fmt"

func maskPII(s string) string {
	isEmail := false
	var result []byte

	if (s[len(s)-1] >= 'a' && s[len(s)-1] <= 'z') || (s[len(s)-1] >= 'A' && s[len(s)-1] <= 'Z') {
		isEmail = true
	}

	if isEmail {
		lower := s[0]
		if lower >= 'A' && lower <= 'Z' {
			lower += 32
		}
		prefix := []byte{lower, '*', '*', '*', '*', '*'}
		result = append(result, prefix...)
		for i := range s {
			if s[i] == '@' {
				for j := i - 1; j < len(s); j++ {
					lower := s[j]
					if lower >= 'A' && lower <= 'Z' {
						lower += 32
					}
					result = append(result, lower)
				}
				break
			}
		}
	} else {
		for i := range s {
			switch s[i] {
			case '+', '-', '(', ')', ' ':
			default:
				result = append(result, s[i])
			}
		}
		prefix := []byte{}

		switch len(result) {
		case 11:
			prefix = []byte{'+', '*'}
		case 12:
			prefix = []byte{'+', '*', '*'}
		case 13:
			prefix = []byte{'+', '*', '*', '*'}
		default:
		}
		if len(prefix) != 0 {
			prefix = append(prefix, '-')
		}
		suffix := result[len(result)-4:]
		result = append(prefix, []byte("***-***-")...)
		result = append(result, suffix...)
	}
	return string(result)
}

func main() {
	fmt.Println(maskPII("LeetCode@LeetCode.com"))
	fmt.Println(maskPII("AB@qq.com"))
	fmt.Println(maskPII("+5(4266)719-677-"))
}
