#!/usr/bin/env python3
# https://adventofcode.com/2021/day/8#part2

import json

from common import read_input, debug_print

INPUT_FILE = '../input/8.txt'

def parse_line(line):
    signals, output = line.split('|')
    signals = signals.strip().split()
    output = output.strip().split()
    assert len(signals) == 10
    assert len(output) == 4
    return signals, output

def parse_input(input_file):
    lines = read_input(input_file)
    entries = []
    for line in lines:
        signals, output = parse_line(line)
        entries.append((signals, output))
    return entries

def sortstring(string):
    return ''.join(sorted(string))

def strissuperset(large, small):
    a = set(large)
    b = set(small)
    return a.issuperset(b)

class SignalDecoder:
    """
    (Step 1)
    Starting condition.
    Knowns: [ 1, 4, 7, 8 ]
         .
        . .
         .
        . .
         .

    (Step 2)
    Combining "7" and "1" (both known), we get the top element
    Knowns: [ 1, 4, 7, 8 ]
         X
        . .
         .
        . .
         .

    (Step 3)
    Then, given we know "1", we can tell which of the 6-element
    numbers is 6, since it's the only 6-element number not to contain both
    elements from "1. Coincidentally, that also gives us another known spot.
    Knowns: [ 1, 4, 7, 8, 6***]

         .             X
        . X           . X
         .      =>     .
        . .           . .
         .             .

    (Step 4)
    With those two in place, we can identify the third element from "7".
    Knowns: [ 1, 4, 6, 7, 8 ]

         .             X
        . .           . X
         .      =>     .
        . X           . X
         .             .

    (Step 5)
    Now, 4 will only have one element that is not in both "0" and "9". That element
    is the middle line. The 6-element that doesn't match "4" is known now too it's "0".
    Knowns: [ 0, 1, 4, 6, 7, 8, 9]
    Remaining: [2, 3, 5]
         .             X
        . .           . X
         X      =>     X
        . .           . X
         .             .

    (Step 6)
    Of the remaining numbers, only one will have precisely one unknown slot, "3".
    This gives us both the number "3" as well as the bottom rung of the number.
    Knowns: [ 0, 1, 3, 4, 7, 8, 6, 9]
    Remaining: [2, 5]
         .             X
        . .           . X
         .      =>     X
        . .           . X
         X             X

    (Step 7)
    Of the two remaining, we can identify "5" because it will differ from "6" by only
    one value. This also provides the remaining two unknown fields.
    Knowns: [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    Remaining: []
         .             X
        X .           X X
         .      =>     X
        X .           X X
         .             X
    """
    def __init__(self, signals):
        assert len(signals) == 10
        self.signals = signals
        """
         aaaa
        b    c
        b    c
         dddd
        e    f
        e    f
         gggg
        """
        # position 'a' will map to some other letter
        self.knowns = {
            'a': False,
            'b': False,
            'c': False,
            'd': False,
            'e': False,
            'f': False,
            'g': False,
        }
        self.numbers = { i: '' for i in range(10) }

        knowns = self.knowns
        numbers = self.numbers

        # Step 1: identify known/unique values
        for s in signals:
            if len(s) == 2:
                self.numbers[1] = sortstring(s)
            elif len(s) == 3:
                self.numbers[7] = sortstring(s)
            elif len(s) == 4:
                self.numbers[4] = sortstring(s)
            elif len(s) == 7:
                self.numbers[8] = sortstring(s)

        # Step 2:
        diff = set(numbers[1]).symmetric_difference(set(numbers[7]))
        assert len(diff) == 1
        self.knowns['a'] = diff.pop()

        # Step 3:
        for s in signals:
            if not len(s) == 6:
                continue
            if strissuperset(s, numbers[1]):
                continue
            numbers[6] = sortstring(s)
            knowns['c'] = (set(numbers[1]) - set(numbers[6])).pop()
        assert self.numbers[6]

        # Step 4:
        knowns['f'] = (set(numbers[7]) - set(knowns['a'] + knowns['c'])).pop()

        # Step 5:
        for s in signals:
            if not len(s) == 6:
                continue
            if numbers[6] == sortstring(s):
                # we already know 6
                continue
            if strissuperset(s, numbers[4]):
                numbers[9] = sortstring(s)
            else:
                numbers[0] = sortstring(s)
                diff = set(numbers[4]) - set(numbers[0])
                assert len(diff) == 1
                knowns['d'] = diff.pop()
        # checkpoint
        for i in [0, 1, 4, 6, 7, 8, 9]:
            assert numbers[i]
        for i in [2, 3, 5]:
            assert not numbers[i]
        for c in ['a', 'c', 'd', 'f']:
            assert knowns[c]
        for c in ['b', 'e', 'g']:
            assert not knowns[c]

        # Step 6:
        # We know characters in position A, C, D, and F. Of the
        # signals that we have not classified, only one should be
        # missing exactly one known position. This will be "3", and
        # give us the G slot.
        known_chars = [ knowns[c] for c in ['a', 'c', 'd', 'f'] ]
        for s in signals:
            if sortstring(s) in numbers.values():
                continue
            unknowns = []
            for char in s:
                if char not in known_chars:
                    unknowns.append(char)
            if len(unknowns) == 1:
                knowns['g'] = unknowns[0]
                numbers[3] = sortstring(s)
        assert numbers[3]
        assert not numbers[2]
        assert not numbers[5]

        # Step 7: Of the two remaining ("2", "5"), we can identify "5" because
        # it will differ from "6" by only one value.
        for s in signals:
            if sortstring(s) in numbers.values():
                continue
            diff = set(s).symmetric_difference(numbers[6])
            if len(diff) == 1:
                numbers[5] = sortstring(s)
                knowns['e'] = diff.pop()
            else:
                numbers[2] = sortstring(s)
                # wait to fill in 'b'


        # Now the only remaining value must be for slot B
        assert not knowns['b']
        rem = set('abcdefg') - set(knowns.values())
        assert len(rem) == 1
        knowns['b'] = rem.pop()

        # Everything should be populated
        for x in knowns:
            assert knowns[x]
        for x in numbers:
            assert numbers[x]

    def debug_print(self):
        debug_print(f'numbers = {json.dumps(self.numbers, indent=4, sort_keys=True)}')
        debug_print(f'knowns = {json.dumps(self.knowns, indent=4, sort_keys=True)}')

    def code_to_digit(self, code):
        for n, sorted_code in self.numbers.items():
            if sorted_code == sortstring(code):
                return n
        assert False, "didn't find code"

def main():
    entries = parse_input(INPUT_FILE)
    running_sum = 0
    for entry in entries:
        signals, outputs = entry
        decoder = SignalDecoder(signals)
        decoder.debug_print()
        output = ''
        for code in outputs:
            digit = decoder.code_to_digit(code)
            output += str(digit)
        debug_print(output)
        running_sum += int(output)
    print(running_sum)

if __name__ == '__main__':
    main()
