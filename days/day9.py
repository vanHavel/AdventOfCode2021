from aocd import get_data, submit
from collections import deque

DAY = 9
YEAR = 2021


def part1(data: str) -> str:
    ans = 0
    lines = data.splitlines()
    grid = [[int(n) for n in line] for line in lines]
    print(grid)
    width = len(grid[0])
    height = len(grid)
    good = lambda x, y: x >= 0 and x < width and y >= 0 and y < height
    for y in range(height):
        for x in range(width):
            ok = True
            for neighbor in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
                ny, nx = neighbor
                if good(nx, ny) and grid[ny][nx] <= grid[y][x]:
                    ok = False
            if ok:
                ans += grid[y][x] + 1
    return str(ans)


def part2(data: str) -> str:
    lows = []
    lines = data.splitlines()
    grid = [[int(n) for n in line] for line in lines]
    width = len(grid[0])
    height = len(grid)
    good = lambda x, y: x >= 0 and x < width and y >= 0 and y < height
    for y in range(height):
        for x in range(width):
            ok = True
            for neighbor in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
                ny, nx = neighbor
                if good(nx, ny) and grid[ny][nx] <= grid[y][x]:
                    ok = False
            if ok:
                lows.append((y, x))
    basins = []
    for low in lows:
        sz = 0
        y, x = low
        q = deque()
        q.append((y, x))
        visited = set()
        visited.add((y, x))
        while len(q) != 0:
            y, x = q.popleft()
            sz += 1
            for neighbor in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
                ny, nx = neighbor
                if good(nx, ny) and (ny, nx) not in visited and grid[ny][nx] < 9:
                    q.append((ny, nx))
                    visited.add((ny, nx))
        basins.append(sz)
    basins = sorted(basins, reverse=True)
    ans = basins[0]*basins[1]*basins[2]
    return str(ans)


if __name__ == '__main__':
    input_data = get_data(day=DAY, year=YEAR)
    ans1 = part1(input_data)
    #submit(answer=ans1, day=DAY, year=YEAR, part=1)
    ans2 = part2(input_data)
    submit(answer=ans2, day=DAY, year=YEAR, part=2)
