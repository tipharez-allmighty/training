package main

import (
	"fmt"
	"strconv"
	"strings"
)

func exclusiveTime(n int, logs []string) []int {
	result := make([]int, n)
	stack := []int{}
	prevTime := 0
	for _, log := range logs {
		currentRecord := strings.Split(log, ":")
		funcNumber, errOne := strconv.Atoi(currentRecord[0])
		funcExecTime, errTwo := strconv.Atoi(currentRecord[2])
		duration := funcExecTime - prevTime
		if errOne != nil || errTwo != nil {
			panic("something went wrong")
		}
		switch currentRecord[1] {
		case "start":
			if len(stack) > 0 {
				result[stack[len(stack)-1]] += duration
			}
			stack = append(stack, funcNumber)
			prevTime = funcExecTime
		case "end":
			currentFunc := stack[len(stack)-1]
			result[currentFunc] += funcExecTime - prevTime + 1
			stack = stack[:len(stack)-1]
			prevTime = funcExecTime + 1

		}
	}
	return result
}

func main() {
	n := 2
	logs := []string{"0:start:0", "1:start:2", "1:end:5", "0:end:6"}
	fmt.Println(exclusiveTime(n, logs))
}
