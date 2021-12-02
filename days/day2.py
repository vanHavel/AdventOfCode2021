from aocd import get_data, submit

DAY = 2
YEAR = 2021


def part1(data: str) -> str:
    cmds = data.splitlines()
    x = 0
    y = 0
    for cmd in cmds:
        text, num = cmd.split(' ')
        num = int(num)
        if text == 'forward':
            x += num
        elif text == 'down':
            y += num
        elif text == 'up':
            y -= num
    ans = x * y
    return str(ans)


def part2(data: str) -> str:
    cmds = data.splitlines()
    x = 0
    y = 0
    aim = 0
    for cmd in cmds:
        text, num = cmd.split(' ')
        num = int(num)
        if text == 'forward':
            x += num
            y += aim * num
        elif text == 'down':
            aim += num
        elif text == 'up':
            aim -= num
    ans = x * y
    return str(ans)


if __name__ == '__main__':
    input_data = get_data(day=DAY, year=YEAR)
    ans1 = part1(input_data)
    submit(answer=ans1, day=DAY, year=YEAR, part=1)
    # ans2 = part2(input_data)
    # submit(answer=ans2, day=DAY, year=YEAR, part=2)
