#!/usr/bin/env python3
# https://adventofcode.com/2021/day/6#part2
# Take a different approach. We don't need to track every fish,
# we just need to track the total number belonging to each day.

INPUT_FILE ='../input/6.txt'
N_DAYS = 256

from common import read_input, debug_print

def parse_input(input_file):
    lines = read_input(input_file)
    assert len(lines) == 1
    return [ int(x) for x in lines[0].split(',') ]

def tick(fish):
    """
    Input: An array of fish ages, each index representing days til birth of a new fish,
    and each value representing the number of fish in that population associated
    with that age value.
    Output: The same array, modified to represent the passage of one day.
    """
    new_fish = fish[0]
    for i in range(8): # decrement ages
        fish[i] = fish[i+1]
    fish[8] = new_fish # set initial counter for new fish
    fish[6] += new_fish # reset counters for parent fish

def main():
    fish_ages = parse_input(INPUT_FILE)
    fish = [0] * 9 # 0 - 8
    for age in fish_ages:
        fish[age] += 1
    for i in range(N_DAYS):
        tick(fish)
    print(sum(fish))

if __name__ == '__main__':
    main()
