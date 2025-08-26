// Two Sum
func twoSum(nums []int, target int) []int {
	seen := make(map[int]int)

	for idx, value := range nums {
		complement := target - value
		if _, ok := seen[complement]; ok {
			return []int{seen[complement], idx}
		}
		seen[value] = idx
	}
	return nil    
}

// Factorial
// Recursive
func factorial(n int) int {
	if n == 0 {
		return 1
	}
	if n <= 2 {
		return n
	}
	return n * (factorial(n - 1))
}

// Fibonacci
// Recursive
func fib(n int) int {
	if n < 2 {
		return n
	}
	return fib(n-2) + fib(n-1)
}

// Tabulation
func fibTab(n int) int {
	if n == 0 {
		return n
	}
	tab := []int{0, 1}
	for i := 2; i < n+1; i++ {
		tab = append(tab, tab[i-1]+tab[i-2])
	}
	return tab[n]
}
