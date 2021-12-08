#!/usr/bin/env python3
# https://adventofcode.com/2021/day/2#part2

INPUT_FILE ='../input/2.txt'

def parse_file(input_file):
    """
    Input: A file containing one direction and unit per line
    Output: An iterable of (direction, unit)
    Blank lines and lines starting with '#' are ignored
    """
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            direction, unit = line.split()
            yield (direction, int(unit))

def calculate_directions(directions):
    """
    Input: An iterable of (direction, unit)
    Output: A summarized collection of directions (x, y)
    """
    x = 0
    y = 0
    aim = 0
    for direction, unit in directions:
        assert direction in ['forward', 'down', 'up']
        if direction == 'forward':
            x += unit
            y += (aim * unit)
        elif direction == 'down':
            aim += unit
        elif direction == 'up':
            aim -= unit
    return x, y

def main():
    directions = parse_file(INPUT_FILE)
    x, y = calculate_directions(directions)
    print(f'({x}, {y}) == {x * y}')


if __name__ == '__main__':
    main()
