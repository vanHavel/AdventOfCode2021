import copy
from typing import Tuple

from aocd import get_data, submit

DAY = 13
YEAR = 2021


def part(data: str) -> Tuple[str, str]:
    lines = data.splitlines()
    points = set()
    folds = []
    for line in lines:
        if "," in line:
            x, y = line.split(",")
            points.add((int(x), int(y)))
        elif "fold" in line:
            _, _, exp = line.split()
            co, num = exp.split("=")
            folds.append((co, int(num)))
    for index, fold in enumerate(folds):
        co, num = fold
        newpoints = copy.copy(points)
        if co == "x":
            for point in points:
                x, y = point
                if x > num:
                    diff = x - num
                    nx = num - diff
                    newpoints.remove((x, y))
                    newpoints.add((nx, y))
        elif co == "y":
            for point in points:
                x, y = point
                if y > num:
                    diff = y - num
                    ny = num - diff
                    newpoints.remove((x, y))
                    newpoints.add((x, ny))
        points = newpoints
        if index == 0:
            ans = len(points)

    width = max([point[0] for point in points]) + 1
    height = max([point[1] for point in points]) + 1
    grid = [["." for x in range(width)] for y in range(height)]
    for point in points:
        x, y = point
        grid[y][x] = "#"
    pp = "\n".join(map(lambda l: "".join(map(str, l)), grid))
    return str(ans), pp


if __name__ == '__main__':
    input_data = get_data(day=DAY, year=YEAR)
    ans1, pp = part(input_data)
    print(pp)
    #submit(answer=ans1, day=DAY, year=YEAR, part=1)
    #submit(answer=ans2, day=DAY, year=YEAR, part=2)
