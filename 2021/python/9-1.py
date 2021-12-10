#!/usr/bin/env python3
# https://adventofcode.com/2021/day/9

from common import read_input

FILE = '9.txt'

def parse_input(filepath):
    return [ [ int(char) for char in line ] for line in read_input(filepath) ]

def get_adjacents(grid, x, y):
    adjacents = []
    # left, right, up, down
    if x > 0:
        adjacents.append(grid[y][x-1])
    if x < len(grid[y]) - 1:
        adjacents.append(grid[y][x+1])
    if y > 0:
        adjacents.append(grid[y-1][x])
    if y < len(grid) - 1:
        adjacents.append(grid[y+1][x])
    return adjacents

def get_risk_level(grid):
    """
    Input: grid of heights
    Sum the 'risk level' (height + 1) for each low point,
    where a low point is any point which has a lesser value
    then all adjacent locations (where adjacent does not include
    diagonals)
    """
    risk = 0
    for y in range(len(grid)):
        for x in (range(len(grid[y]))):
            height = grid[y][x]
            if height < min(get_adjacents(grid, x, y)):
                risk += height + 1
    return risk

def main():
    grid = parse_input(FILE)
    lp = get_risk_level(grid)
    print(lp)

if __name__ == '__main__':
    main()
