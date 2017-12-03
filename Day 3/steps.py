# Day 3: Spiral Memory
# https://adventofcode.com/2017/day/3
import sys
from math import sqrt, floor, ceil

def main():
    size = int(sys.argv[1])

    root = ceil(sqrt(size))
    diameter = root + 1 if root % 2 == 0 else root # always odd diameter (1, 3, 5, ..)
    packet_size = diameter - 1
    radius = floor(diameter/2)

    # Every time the diameter gets bigger we update the reference
    reference = (diameter - 2)**2 # Reference = the square on the hot bottom right corner
    index_in_paquet = abs(size - (reference+radius))

    steps = radius + index_in_paquet % packet_size
    print('Part one: '+ str(steps))

if __name__ == '__main__': 
    main()