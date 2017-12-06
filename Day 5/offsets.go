package main

import (
	"fmt"
	"log"
	"os"
	"bufio"
	"strconv"
)

func main() {
	fmt.Println("Part one:", countJumpsOne(getNumbers(), 0, 0))
	fmt.Println("Part two:", countJumpsTwo(getNumbers()))
}

// Recursive index bounce
// Part one
func countJumpsOne(offsets []int, index int, count int) int {
	if index < 0 || index >= len(offsets) {
		return count
	}

	new_index := index + offsets[index]
	offsets[index]++
	count++

	return countJumpsOne(offsets, new_index, count)
}

// Not recursive this time
// About 28 millions loops so huge cost in memory
func countJumpsTwo(offsets []int) int {
	count := 0
	index := 0

	for {
		if index < 0 || index >= len(offsets) {
			return count
		}

		old := index
		index = index + offsets[index]
		if offsets[old] >= 3 {
			offsets[old]--
		} else {
			offsets[old]++
		}
		count++
	}
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