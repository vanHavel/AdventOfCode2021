from aocd import get_data, submit

DAY = 25
YEAR = 2021


def part1(data: str) -> str:
    lines = data.splitlines()
    width = len(lines[0])
    height = len(lines)
    grid = [[c for c in line] for line in lines]
    change = True
    steps = 0
    while change:
        change = False
        steps += 1
        moves = []
        for i in range(height):
            for j in range(width):
                nj = (j+1) % width
                if grid[i][j] == ">" and grid[i][nj] == ".":
                    change = True
                    moves.append((i, j))
        for i, j in moves:
            nj = (j+1) % width
            grid[i][nj] = ">"
            grid[i][j] = "."
        moves = []
        for i in range(height):
            for j in range(width):
                ni = (i+1) % height
                if grid[i][j] == "v" and grid[ni][j] == ".":
                    change = True
                    moves.append((i, j))
        for i, j in moves:
            ni = (i+1) % height
            grid[ni][j] = "v"
            grid[i][j] = "."
    print(steps)
    return str(steps)

if __name__ == '__main__':
    input_data = get_data(day=DAY, year=YEAR)
    ans1 = part1(input_data)
    submit(answer=ans1, day=DAY, year=YEAR, part=1)
