#!/usr/bin/env python3
# https://adventofcode.com/2021/day/7

from common import read_input

INPUT_FILE ='../input/7.txt'

def parse_input(input_file):
    lines = read_input(input_file)
    assert len(lines) == 1
    return [int(x) for x in lines[0].split(',')]

def get_median(array):
    middle_index = (len(array) // 2) - 1
    return sorted(array)[middle_index]

def main():
    positions = parse_input(INPUT_FILE)
    median = get_median(positions)
    distance = 0
    for pos in positions:
        distance += abs(pos - median)
    print(distance)

if __name__ == '__main__':
    main()
