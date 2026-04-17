package main

import "fmt"

func countStudents(students []int, sandwiches []int) int {
	rotations := 0
	for len(sandwiches) > 0 && rotations < len(students) {
		topSandwich := sandwiches[0]
		currentStudent := students[0]
		students = students[1:]
		if currentStudent == topSandwich {
			sandwiches = sandwiches[1:]
			rotations = 0
		} else {
			students = append(students, currentStudent)
			rotations++
		}
	}
	return len(students)
}

func countStudentsTwo(students []int, sandwiches []int) int {
	preferenceCounts := [2]int{0, 0}
	for _, studentPreference := range students {
		preferenceCounts[studentPreference]++
	}
	for _, sandwich := range sandwiches {
		if preferenceCounts[sandwich] == 0 {
			break
		}
		preferenceCounts[sandwich]--
	}
	return preferenceCounts[0] + preferenceCounts[1]
}

func main() {
	fmt.Println(countStudentsTwo([]int{1, 1, 1, 0, 0, 1}, []int{1, 0, 0, 0, 1, 1}))
}
