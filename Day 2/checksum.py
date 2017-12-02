# Day 2: Corruption Checksum
# http://adventofcode.com/2017/day/2
from itertools import combinations

def can_divide(x,y): 
    return x % y == 0

def divisible_numbers(numbers):
    total = 0 
    for num1, num2 in combinations(numbers, 2):
        if can_divide(num1,num2): 
            total += num1 / num2
        if can_divide(num2,num1):
            total += num2 / num1
    return int(total)

def main(): 
    total_one = 0
    total_two = 0

    with open('input.txt', 'r') as file: 
        for row in file: 
            numbers = [int(i) for i in row.split()]
            # Part one 
            total_one += max(numbers) - min(numbers)
            # Part two 
            total_two += divisible_numbers(numbers)

    print("Part one: " + str(total_one))
    print("Part two: " + str(total_two))

if __name__ == '__main__': 
  main()