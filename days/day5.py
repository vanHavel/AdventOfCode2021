from collections import defaultdict
from typing import List, Tuple

from aocd import get_data, submit

DAY = 5
YEAR = 2021


def part1(data: str) -> str:
    segments = read(data)
    covered = defaultdict(int)
    for segment in segments:
        x1, y1, x2, y2 = segment
        if x1 != x2 and y1 != y2:
            continue
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                covered[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                covered[(x, y1)] += 1
    ans = 0
    for point in covered:
        if covered[point] > 1:
            ans += 1
    return str(ans)


def part2(data: str) -> str:
    segments = read(data)
    covered = defaultdict(int)
    for segment in segments:
        x1, y1, x2, y2 = segment
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                covered[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                covered[(x, y1)] += 1
        else:
            if x1 > x2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            if y1 < y2:
                for x in range(x1, x2+1):
                    covered[(x, y1+(x-x1))] += 1
            else:
                for x in range(x1, x2+1):
                    covered[(x, y1-(x-x1))] += 1
    ans = 0
    for point in covered:
        if covered[point] > 1:
            ans += 1
    return str(ans)


def read(data: str) -> List[Tuple[int, int, int, int]]:
    lines = data.splitlines()
    segments = []
    for line in lines:
        left, right = line.split('->')
        x1, y1 = left.split(',')
        x2, y2 = right.split(',')
        segments.append((int(x1), int(y1), int(x2), int(y2)))
    return segments


if __name__ == '__main__':
    input_data = get_data(day=DAY, year=YEAR)
    ans1 = part1(input_data)
    print(ans1)
    #submit(answer=ans1, day=DAY, year=YEAR, part=1)
    ans2 = part2(input_data)
    print(ans2)
    submit(answer=ans2, day=DAY, year=YEAR, part=2)
