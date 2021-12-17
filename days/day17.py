from typing import Tuple

from aocd import get_data, submit

DAY = 17
YEAR = 2021


def part1(data: str) -> Tuple[str, str]:
    _, _, xp, yp = data.split()
    xp, yp = xp[2:-1], yp[2:]
    xmin, xmax = [int(n) for n in xp.split("..")]
    ymin, ymax = [int(n) for n in yp.split("..")]

    best = 0
    count = 0
    for xcand in range(5, 140):
        for ycand in range(-155, 300):
            xp, yp = 0, 0
            maxy = 0
            xv, yv = xcand, ycand
            for step in range(500):
                xp += xv
                yp += yv
                if xv > 0:
                    xv -= 1
                yv -= 1
                maxy = max(maxy, yp)
                if xmin <= xp <= xmax and ymin <= yp <= ymax:
                    count += 1
                    if maxy > best:
                        best = max(best, maxy)
                    break
    return str(best), str(count)


if __name__ == '__main__':
    input_data = get_data(day=DAY, year=YEAR)
    ans1, ans2 = part1(input_data)
    #submit(answer=ans1, day=DAY, year=YEAR, part=1)
    submit(answer=ans2, day=DAY, year=YEAR, part=2)
