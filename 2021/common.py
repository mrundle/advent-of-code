import os

def read_input(input_file, keep_empty=False):
    lines = []
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith('#'):
                continue
            lines.append(line)
    return lines

def debug_print(msg):
    if os.getenv('DEBUG'):
        print(msg if msg else '')
