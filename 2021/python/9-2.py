#!/usr/bin/env python3
# https://adventofcode.com/2021/day/9#part2

import math
from common import read_input, debug_print

FILE = '../input/9.txt'

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

def is_low_point(grid, x, y):
    return grid[y][x] < min(get_adjacents(grid, x, y))

def handle_point(grid, seen, cur_height, x, y, coordinates):
    if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[y]):
        return
    if seen[y][x]:
        return
    if grid[y][x] < cur_height or grid[y][x] >= 9:
        return
    debug_print(f'appending ({x}, {y}) == {grid[y][x]}')
    seen[y][x] = grid[y][x]
    coordinates.append((x, y))

def get_basin_for_lowpoint(grid, x, y):
    """
    This is the bulk of problem 2. What I'm thinking as an approach:
    for each low point, continuously branch out into squares that adhere
    to the following criteria:
        1) height >= current height
        2) height != 9 (max)
        3) not already part of basin
    The trick with the third is that we'll need to keep a shadow grid.
    """
    seen = [ [None for i in range(len(grid[0]))] for j in range(len(grid)) ]
    coordinates = [(x, y),]
    basin_size = 0
    while coordinates:
        basin_size += 1
        x, y = coordinates.pop()
        height = grid[y][x]
        seen[y][x] = str(height)
        handle_point(grid, seen, height, x-1, y, coordinates)
        handle_point(grid, seen, height, x+1, y, coordinates)
        handle_point(grid, seen, height, x, y-1, coordinates)
        handle_point(grid, seen, height, x, y+1, coordinates)
    for row in seen:
        debug_print(''.join([x if x else '.' for x in row]))
    return basin_size

def get_largest_basins(grid, n):
    """
    Input: grid of heights
    Sum the 'risk level' (height + 1) for each low point,
    where a low point is any point which has a lesser value
    then all adjacent locations (where adjacent does not include
    diagonals)
    """
    basin_sizes = []
    for y in range(len(grid)):
        for x in (range(len(grid[y]))):
            if is_low_point(grid, x, y):
                basin_size = get_basin_for_lowpoint(grid, x, y)
                basin_sizes.append(basin_size)
                debug_print(f'basin_size = {basin_size}')
                debug_print('==========\n')
    return math.prod(sorted(basin_sizes)[-n:])

def main():
    grid = parse_input(FILE)
    n = get_largest_basins(grid, 3)
    print(n)

if __name__ == '__main__':
    main()
