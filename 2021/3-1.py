#!/usr/bin/env python3
# https://adventofcode.com/2021/day/3

INPUT_FILE = '3.txt'

def parse_file(input_file):
    """
    Input: A file containing one binary-number string per line
    Output: A list of binary number strings
    Blank lines and lines starting with '#' are ignored
    """
    strings = []
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            if line and not line.startswith('#'):
                strings.append(line)
    return strings

def calculate(strings):
    n_strings = len(strings)
    pos = 0
    max_pos = len(strings[0])
    gamma = ''
    epsilon = ''
    for pos in range(max_pos):
        n = 0
        for string in strings:
            n += string[pos] == '1'
        if n >= (n_strings / 2):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    _gamma = int(gamma, 2)
    _epsilon = int(epsilon, 2)
    print(f'{gamma} == {_gamma}')
    print(f'{epsilon} == {_epsilon}')
    return _gamma * _epsilon

def main():
    strings = parse_file(INPUT_FILE)
    result = calculate(strings)
    print(result)

if __name__ == '__main__':
    main()
