#!/usr/bin/env python3
# https://adventofcode.com/2021/day/10

from common import read_input

FILE = '../input/10.txt'

match = {
    '[': ']',
    '(': ')',
    '{': '}',
    '<': '>',
}

score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

def syntax_error_score(line):
    stack = []
    for char in line:
        if char in match.keys():
            stack.append(char)
        elif char != match[stack.pop()]:
            return score[char]
    return 0

def main():
    lines = read_input(FILE)
    score = sum([ syntax_error_score(line) for line in lines ])
    print(score)

if __name__ == '__main__':
    main()
