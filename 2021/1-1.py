#!/usr/bin/env python3
# https://adventofcode.com/2021/day/1

INPUT_FILE = '1-1.txt'

def file_to_ints(input_file):
    """
    Input: A file containing one number per line
    Output: An int iterable
    Blank lines and lines starting with '#' are ignored
    """
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            if line and not line.startswith('#'):
                yield int(line)

def get_increases(array):
    """
    Input: An array of numbers
    Output: The number of elements larger than the one preceding it
    """
    prev = None
    inc = 0
    for n in array:
        if prev and n > prev:
            inc += 1
        prev = n
    return inc

def main():
    depths = file_to_ints(INPUT_FILE)
    increases = get_increases(depths)
    print(increases)

if __name__ == '__main__':
    main()
