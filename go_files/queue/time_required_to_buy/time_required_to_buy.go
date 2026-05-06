package main

import "fmt"

func timeRequiredToBuy(tickets []int, k int) int {
	currentKindex := k
	currentTime := 0
	i := 0
	for len(tickets) > 0 {
		currentTime++
		currentValue := tickets[i] - 1
		tickets = tickets[1:]
		if currentValue > 0 {
			tickets = append(tickets, currentValue)
		} else if currentValue == 0 && i == currentKindex {
			break
		} else if len(tickets) == 1 && i == currentKindex {
			currentTime += currentValue
			break
		}
		if i == currentKindex {
			currentKindex = len(tickets) - 1
		} else {
			currentKindex--
		}
	}
	return currentTime
}

func betterTimeRequiredToBuy(tickets []int, k int) int {
	targetValue := tickets[k]
	currentTime := 0
	for idx, val := range tickets {
		if idx <= k {
			currentTime += min(targetValue, val)
		} else {
			currentTime += min(targetValue-1, val)
		}
	}
	return currentTime
}

func main() {
	tickets := []int{5, 1, 1, 1}
	k := 0
	fmt.Println(betterTimeRequiredToBuy(tickets, k))
}
