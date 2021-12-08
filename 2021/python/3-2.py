#!/usr/bin/env python3
# https://adventofcode.com/2021/day/3#part2
# This one was just off the wall

INPUT_FILE ='../input/3.txt'

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

def get_rating(strings, keep_larger=True):
    assert len(strings) > 1
    n_bits = len(strings[0])
    for pos in range(n_bits):
        ones = 0
        zeroes = 0
        remaining_strings = []
        for string in strings:
            assert string[pos] in ['0', '1']
            if string[pos] == '1':
                ones += 1
            else:
                zeroes += 1
        for string in strings:
            if keep_larger:
                keep = '1' if ones >= zeroes else '0'
            else:
                keep = '1' if ones < zeroes else '0'
            if string[pos] == keep:
                remaining_strings.append(string)
        strings = remaining_strings
        if len(strings) == 1:
            return int(strings[0], 2)

def main():
    strings = parse_file(INPUT_FILE)
    o2 = get_rating(strings, keep_larger=True)
    co2 = get_rating(strings, keep_larger=False)
    print(f'oxygen_generator_rating = {o2}')
    print(f'co2_scrubber_rating = {co2}')
    print(o2 * co2)

if __name__ == '__main__':
    main()
