from aocd import get_data, submit
import numpy as np

DAY = 7
YEAR = 2021


def part1(data: str) -> str:
    nums = [int(n) for n in data.split(',')]
    median = int(np.median(nums))
    ans = 0
    for i in nums:
        ans += abs(i - median)
    return str(ans)


def part2(data: str) -> str:
    nums = [int(n) for n in data.split(',')]
    mean = round(np.mean(nums)) - 1
    ans = 0
    for i in nums:
        d = abs(i - mean)
        ans += d * (d+1) // 2
    return str(ans)


if __name__ == '__main__':
    input_data = get_data(day=DAY, year=YEAR)
    ans1 = part1(input_data)
    #submit(answer=ans1, day=DAY, year=YEAR, part=1)
    ans2 = part2(input_data)
    submit(answer=ans2, day=DAY, year=YEAR, part=2)
