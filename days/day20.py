from aocd import get_data, submit

DAY = 20
YEAR = 2021


def part(data: str, steps: int) -> str:
    enhances, ii = data.split("\n\n")
    enhancej = "".join(enhances.splitlines())
    enhance = [1 if c == "#" else 0 for c in enhancej]

    grid = set()
    for y, line in enumerate(ii.splitlines()):
        for x, c in enumerate(line):
            if c == "#":
                grid.add((y, x))

    default = 0
    for step in range(steps):
        newgrid = set()
        miny = min(t[0] for t in grid) - 1
        minx = min(t[1] for t in grid) - 1
        maxy = max(t[0] for t in grid) + 1
        maxx = max(t[1] for t in grid) + 1

        for y in range(miny, maxy + 1):
            for x in range(minx, maxx + 1):
                bins = []
                for y2 in range(y-1, y+2):
                    for x2 in range(x-1, x+2):
                        bins.append(1 - default if (y2, x2) in grid else default)
                bini = int("".join(map(str, bins)), 2)
                target = enhance[bini]
                if target == default:
                    newgrid.add((y, x))

        grid = newgrid
        default = 1 - default

    return str(len(grid))


if __name__ == '__main__':
    input_data = get_data(day=DAY, year=YEAR)
    ans1 = part(input_data, 2)
    #submit(answer=ans1, day=DAY, year=YEAR, part=1)
    ans2 = part(input_data, 50)
    submit(answer=ans2, day=DAY, year=YEAR, part=2)
