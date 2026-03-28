package main

import (
	"fmt"
	"strconv"
)

func evalRPN(tokens []string) int {
	stack := []int{}
	for _, operand := range tokens {
		operandInt, err := strconv.Atoi(operand)
		if err != nil {
			result := 0
			numberTwo := stack[len(stack)-1]
			numberOne := stack[len(stack)-2]
			stack = stack[:len(stack)-2]
			switch operand {
			case "+":
				result = numberOne + numberTwo
			case "-":
				result = numberOne - numberTwo
			case "*":
				result = numberOne * numberTwo
			case "/":
				result = numberOne / numberTwo
			default:
				panic(fmt.Sprintf("%v operand is not supported.", operand))
			}
			stack = append(stack, result)
		} else {
			stack = append(stack, operandInt)
		}
	}
	return stack[0]
}

func main() {
	tokens := []string{"4", "13", "5", "/", "+"}
	fmt.Println(evalRPN(tokens))
}
