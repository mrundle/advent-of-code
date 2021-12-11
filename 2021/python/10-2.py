#!/usr/bin/env python3
# https://adventofcode.com/2021/day/10#part2

from common import read_input

FILE = '../input/10.txt'

match = {
    '[': ']',
    '(': ')',
    '{': '}',
    '<': '>',
}

scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def completion_score(line):
    stack = []
    for char in line:
        if char in match.keys():
            stack.append(char)
        elif char != match[stack.pop()]:
            return 0 # corrupt, discard
    score = 0
    while stack:
        score = (5 * score) + scores[match[stack.pop()]]
    return score

def main():
    lines = read_input(FILE)
    scores = []
    for line in lines:
        score = completion_score(line)
        if score:
            scores.append(score)
    print(sorted(scores)[len(scores)//2])

if __name__ == '__main__':
    main()
