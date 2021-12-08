#!/usr/bin/env python3
# https://adventofcode.com/2021/day/5
# Probably some smarter way, but I'm going 2D array

from common import read_input, debug_print

INPUT_FILE ='../input/5.txt'

def parse_input(input_file):
    max_index = 0
    lines = []
    for line in read_input(input_file):
        src, dst = [
            [
                int(n) for n in x.strip().split(',')
            ] for x in line.split('->')
        ]
        max_index = max(max_index, max(max(src), max(dst)))
        lines.append((src, dst))
    return lines, max_index

def get_range(a, b):
    if a <= b:
        return list(range(a, b + 1, 1))
    else:
        return list(range(a, b - 1, -1))

def build_grid(lines, max_index):
    grid_len = max_index + 1
    grid = [ [0] * grid_len for i in range(grid_len) ]
    for line in lines:
        src, dst = line
        msg = f'processing {src}, {dst} '
        if src[0] == dst[0]: # vertical
            x = src[0]
            for y in get_range(src[1], dst[1]):
                grid[y][x] += 1
            msg += 'vertical'
        elif src[1] == dst[1]: # horizontal
            y = src[1]
            for x in get_range(src[0], dst[0]):
                grid[y][x] += 1
            msg += 'horizontal'
        else:
            x_vals = get_range(src[0], dst[0])
            y_vals = get_range(src[1], dst[1])
            msg += 'diagonal'
            for i in range(len(x_vals)):
                grid[y_vals[i]][x_vals[i]] += 1
                msg += f' ({y_vals[i]}, {x_vals[i]})'
        debug_print(msg)
    return grid

def print_grid(grid):
    for row in grid:
        debug_print(' '.join(['.' if x == 0 else str(x) for x in row]))

def main():
    lines, max_index = parse_input(INPUT_FILE)
    grid = build_grid(lines, max_index)
    res = 0
    for i in range(max_index + 1):
        for j in range(max_index + 1):
            res += grid[i][j] > 1
    print_grid(grid)
    print(res)

if __name__ == '__main__':
    main()
