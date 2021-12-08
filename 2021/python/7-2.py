#!/usr/bin/env python3
# https://adventofcode.com/2021/day/7#part2

from common import read_input, debug_print

INPUT_FILE ='../input/7.txt'

def parse_input(input_file):
    lines = read_input(input_file)
    assert len(lines) == 1
    return [int(x) for x in lines[0].split(',')]

def get_avg(array):
    return sum(array) // len(array)

def get_distance(a, b):
    distance = 0
    for i in range(abs(a - b)):
        distance += i + 1
    debug_print(f'{a} -> {b} = {distance}')
    return distance

def main():
    positions = parse_input(INPUT_FILE)
    avg = get_avg(positions)
    distance = 0
    for pos in positions:
        distance += get_distance(pos, avg)
    print(f'Align at: {avg}')
    print(f'Distance: {distance}')

if __name__ == '__main__':
    main()
