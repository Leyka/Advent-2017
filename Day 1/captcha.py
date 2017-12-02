# Day 1: Inverse Captcha
# http://adventofcode.com/2017/day/1

def compare(data, index_to_compare):
    total = 0
    for index, value in enumerate(data):
        if value == data[ (index + index_to_compare) % len(data) ]: # Circular comparison with last index and first index
            total += int(value)
    return total 

def main():
    with open('input.txt', 'r') as file: 
        data = file.read()
        # Part one
        print("Part one: " + str(compare(data, 1)))
        # Part two
        half_index = int(len(data)/2)
        print("Part two: " + str(compare(data, half_index)))

if __name__ == '__main__': 
    main()