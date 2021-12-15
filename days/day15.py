from aocd import get_data, submit
from util.astar import AStar

DAY = 15
YEAR = 2021


def part1(data: str) -> str:
    lines = data.splitlines()
    grid = [[int(n) for n in line] for line in lines]
    width = len(grid[0])
    height = len(grid)
    start = (0, 0)
    end = (height-1, width-1)
    def succ(pos):
        y, x = pos
        ns = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
        ns = [n for n in ns if n[0] >= 0 and n[0] < height and n[1] >= 0 and n[1] < width]
        ns = [(grid[n[0]][n[1]], n) for n in ns]
        return ns
    def goal(pos):
        return pos == end
    def h(pos):
        y, x = pos
        return abs(height-1-y) + abs(width-1-x)
    astar = AStar(succ, goal, h)
    cost, path = astar.search(start)
    return str(cost)


def part2(data: str) -> str:
    lines = data.splitlines()
    grid = []
    for i in range(5):
        for line in lines:
            grid.append([])
            for j in range(5):
                for char in line:
                    n = int(char)
                    n += i + j
                    if n > 9:
                        n -= 9
                    grid[-1].append(n)
    width = len(grid[0])
    height = len(grid)
    start = (0, 0)
    end = (height-1, width-1)
    def succ(pos):
        y, x = pos
        ns = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
        ns = [n for n in ns if n[0] >= 0 and n[0] < height and n[1] >= 0 and n[1] < width]
        ns = [(grid[n[0]][n[1]], n) for n in ns]
        return ns
    def goal(pos):
        return pos == end
    def h(pos):
        y, x = pos
        return abs(height-1-y) + abs(width-1-x)
    astar = AStar(succ, goal, h)
    cost, path = astar.search(start)
    return str(cost)


if __name__ == '__main__':
    input_data = get_data(day=DAY, year=YEAR)
    ans1 = part1(input_data)
    #submit(answer=ans1, day=DAY, year=YEAR, part=1)
    ans2 = part2(input_data)
    submit(answer=ans2, day=DAY, year=YEAR, part=2)
