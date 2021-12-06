from collections import defaultdict

from aocd import get_data, submit

DAY = 6
YEAR = 2021


def part1(data: str, days: int) -> str:
    fish = defaultdict(int)
    for times in data.split(','):
        n = int(times)
        fish[n] += 1
    for step in range(256):
        new = defaultdict(int)
        for value, count in fish.items():
            if value > 0:
                new[value-1] += count
            else:
                new[6] += count
                new[8] += count
        fish = new
    return str(sum(fish.values()))


if __name__ == '__main__':
    input_data = get_data(day=DAY, year=YEAR)
    ans1 = part1(input_data, days=80)
    submit(answer=ans1, day=DAY, year=YEAR, part=1)
    ans2 = part1(input_data, days=256)
    submit(answer=ans2, day=DAY, year=YEAR, part=2)
