from typing import List, Tuple

from aocd import get_data, submit

DAY = 4
YEAR = 2021


def part1(data: str) -> str:
    draws, boards = read(data)
    markedset = set()
    for draw in draws:
        print('draw ' + str(draw))
        markedset.add(draw)
        for board in boards:
            if bingo(board, markedset):
                unmarked = sum([n for row in board for n in row if n not in markedset])
                print(unmarked)
                score = unmarked * draw
                print('bingo ' + str(score))
                return str(score)


def part2(data: str) -> str:
    draws, boards = read(data)
    markedset = set()
    for draw in draws:
        print('draw ' + str(draw))
        markedset.add(draw)
        for board in boards:
            if bingo(board, markedset):
                unmarked = sum([n for row in board for n in row if n not in markedset])
                print(unmarked)
                score = unmarked * draw
                print('bingo ' + str(score))
                boards.remove(board)
                if len(boards) == 0:
                    return str(score)


def bingo(board: List[List[List[int]]], marked: List[int]) -> bool:
    for row in range(5):
        ok = True
        for col in range(5):
            if board[row][col] not in marked:
                ok = False
        if ok:
            return True
    for col in range(5):
        ok = True
        for row in range(5):
            if board[row][col] not in marked:
                ok = False
        if ok:
            return True
    return False


def read(data: str) -> Tuple[List[int], List[List[List[int]]]]:
    lines = data.splitlines()
    draws = [int(n) for n in lines[0].split(',')]
    lines = lines[2:]
    boards = []
    while lines:
        board = lines[:5]
        iboard = [[int(col) for col in row.split()] for row in board]
        boards.append(iboard)
        lines = lines[6:]
    return draws, boards


if __name__ == '__main__':
    input_data = get_data(day=DAY, year=YEAR)
    #ans1 = part1(input_data)
    #submit(answer=ans1, day=DAY, year=YEAR, part=1)
    ans2 = part2(input_data)
    submit(answer=ans2, day=DAY, year=YEAR, part=2)
