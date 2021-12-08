#!/usr/bin/env python
# https://adventofcode.com/2021/day/4#part2
# Pretty inefficient. Just brute force.

from common import read_input

INPUT_FILE ='../input/4.txt'

BOARD_SIZE = 5
DEBUG_PRINT = False

def debug_print(msg=None):
    if DEBUG_PRINT:
        print(msg if msg else '')

class Board():
    def __init__(self, board):
        self.bingo = False
        self.size = len(board)
        assert self.size == BOARD_SIZE
        for line in board:
            assert len(line) == self.size
        self.board_values = board
        self.board_hits = [ [False] * self.size for i in range(self.size) ]

    def mark(self, value):
        for i in range(self.size):
            for j in range(self.size):
                if str(self.board_values[i][j]) == str(value):
                    self.board_hits[i][j] = True
                    return

    def debug_print(self):
        debug_print()
        for i in range(self.size):
            hits = ' '.join(['1' if x else '0' for x in self.board_hits[i]])
            values = ' '.join([str(x).ljust(3) for x in self.board_values[i]])
            debug_print(f'{hits}\t{values}')
        debug_print()

    def has_bingo(self):
        if self.bingo:
            return True
        # check horizontals and verticals
        for i in range(self.size):
            if all(self.board_hits[i]):
                debug_print(f'horizontal hit: {self.board_values[i]}')
                self.bingo = True
                return True
            if all([ row[i] for row in self.board_hits ]):
                debug_print(f'vertical hit: {[row[i] for row in self.board_values]}')
                self.bingo = True
                return True

    def sum_unmarked(self):
        value = 0
        for i in range(self.size):
            for j in range(self.size):
                if not self.board_hits[i][j]:
                    value += int(self.board_values[i][j])
        return value

def parse_input(input_file):
    lines = read_input(input_file, keep_empty=True)
    n_lines = len(lines)
    lineno = 0
    numbers = [int(x) for x in lines[lineno].split(',')]
    lineno += 1
    # read the boards
    boards = []
    while lineno < n_lines:
        # assert and consume blank line
        assert not lines[lineno]
        lineno += 1
        board = BOARD_SIZE * [BOARD_SIZE * [None]]
        board = []
        for i in range(BOARD_SIZE):
            board.append([ int(x) for x in lines[lineno + i].split()])
        lineno += BOARD_SIZE
        boards.append(Board(board))
    return numbers, boards

def main():
    numbers, boards = parse_input(INPUT_FILE)
    for number in numbers:
        for board in boards:
            if board.has_bingo():
                continue
            board.mark(number)
            if board.has_bingo():
                board.debug_print()
                if len(boards) == 1:
                    return board.sum_unmarked() * number
        boards = [ board for board in boards if not board.has_bingo() ]

if __name__ == '__main__':
    result = main()
    print(result)
