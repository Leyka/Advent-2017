package main

import (
	"fmt"
	"log"
	"os"
	"bufio"
	"strconv"
)

func main() {
	
	numbers := getNumbers()
	jumpCount := jump(numbers, 0, 0)
	fmt.Println("Part one:", jumpCount)

}

// Recursive index bounce
func jump(numbers []int, index int, count int) int {
	if index < 0 || index >= len(numbers) {
		return count
	}

	new_index := index + numbers[index]
	numbers[index]++
	count++

	return jump(numbers, new_index, count)
}

// Read file and return array of numbers
func getNumbers() ([]int) {
	f, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	var numbers []int
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		number,_ := strconv.Atoi(scanner.Text())
		numbers = append(numbers, number)
	}
	return numbers
}

