#!/usr/bin/env python3
from common import read_input, debug_print

INPUT_FILE = 'tmp'
INPUT_FILE = '8.txt'

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

def main():
    entries = parse_input(INPUT_FILE)
    n = 0
    for entry in entries:
        signals, outputs = entry
        debug_print(f'signals={signals}')
        debug_print(f'outputs={outputs}')
        seen = set()
        for output in outputs:
            if len(output) in [2, 4, 3, 7]:
                n += 1
    print(n)



main()
