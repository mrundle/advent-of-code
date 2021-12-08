#!/usr/bin/env python3
# https://adventofcode.com/2021/day/6

INPUT_FILE ='../input/6.txt'
N_DAYS = 80

from common import read_input, debug_print

def parse_input(input_file):
    lines = read_input(input_file)
    assert len(lines) == 1
    return [ int(x) for x in lines[0].split(',') ]

def tick(fish):
    """
    Input: list of numbers representing lanternfish
    Output: the same modified list of lanternfish, progressed by one day
    """
    new_fish = []
    for i in range(len(fish)):
        assert fish[i] >= 0
        if fish[i] > 0:
            fish[i] -= 1
        else:
            fish[i] = 6
            new_fish.append(8)
    fish.extend(new_fish)

def main():
    fish = parse_input(INPUT_FILE)
    for i in range(N_DAYS):
        tick(fish)
        debug_print(f'after {i+1} days: {",".join([str(x) for x in fish])}')
    print(len(fish))

if __name__ == '__main__':
    main()
