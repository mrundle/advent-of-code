#!/usr/bin/env python3
# https://adventofcode.com/2021/day/1#part2

# Implementation note: Part 1 read the file in and acted as a generator
# to provide an integer iterable. This Part 2 implementation reads the
# entire file into an array to make use of a look-ahead. It would be
# neat to continue using the generator approach with sliding windows,
# but I can't immediately think of a clean way to do that.

INPUT_FILE = '1.txt'
WINDOW = 3

def file_to_ints(input_file):
    """
    Input: A file containing one number per line
    Output: An int iterable
    Blank lines and lines starting with '#' are ignored
    """
    ints = []
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            if line and not line.startswith('#'):
                ints.append(int(line))
    return ints

def get_increases(array, window=1):
    """
    Input: An array of numbers
    Output: The number of elements larger than the one preceding it
    """
    prev = None
    inc = 0
    for i in range(len(array) - window + 1):
        n = 0
        for j in range(window):
            n += array[i + j]
        if prev and n > prev:
            inc += 1
        prev = n
    return inc

def main():
    depths = file_to_ints(INPUT_FILE)
    increases = get_increases(depths, window=WINDOW)
    print(increases)

if __name__ == '__main__':
    main()
