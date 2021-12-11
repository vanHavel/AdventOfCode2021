from typing import Tuple

from aocd import get_data, submit

DAY = 11
YEAR = 2021


def part(data: str) -> Tuple[str, str]:
    lines = data.splitlines()
    grid = [[int(c) for c in line] for line in lines]
    height = len(grid)
    width = len(grid[0])
    ans1, ans2 = 0, 0
    for step in range(1000000):
        check = []
        flashed = set()
        local = 0
        for i in range(height):
            for j in range(width):
                grid[i][j] += 1
                if grid[i][j] >= 10:
                    check.append((i, j))
        while check != []:
            i, j = check.pop()
            if (i, j) not in flashed:
                flashed.add((i, j))
                local += 1
                if step < 100:
                    ans1 += 1
                for ni in range(i-1, i+2):
                    for nj in range(j-1, j+2):
                        if ni >= 0 and ni < height and nj >= 0 and nj < width and not (i, j) == (ni, nj):
                            grid[ni][nj] += 1
                            if grid[ni][nj] >= 10 and not (ni, nj) in flashed:
                                check.append((ni, nj))
        for i in range(height):
            for j in range(width):
                if grid[i][j] >= 10:
                    grid[i][j] = 0
        if local == width * height:
            ans2 = step+1
            break
    return str(ans1), str(ans2)


if __name__ == '__main__':
    input_data = get_data(day=DAY, year=YEAR)
    ans1, ans2 = part(input_data)
    submit(answer=ans1, day=DAY, year=YEAR, part=1)
    #submit(answer=ans1, day=DAY, year=YEAR, part=2)
