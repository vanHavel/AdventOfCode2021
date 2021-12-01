from aocd import get_data, submit

DAY = 1
YEAR = 2021


def part1(data: str) -> str:
    nums = [int(n) for n in data.splitlines()]
    ans = 0
    for i in range(len(nums) - 1):
        if nums[i+1] > nums[i]:
            ans += 1
    return str(ans)


def part2(data: str) -> str:
    nums = [int(n) for n in data.splitlines()]
    wins = [sum(nums[i:i+3]) for i in range(len(nums)-2)]
    ans = 0
    for i in range(len(wins) - 1):
        if wins[i + 1] > wins[i]:
            ans += 1
    return str(ans)


if __name__ == '__main__':
    input_data = get_data(day=DAY, year=YEAR)
    ans1 = part1(input_data)
    submit(answer=ans1, day=DAY, year=YEAR, part=1)
    # ans2 = part2(input_data)
    # submit(answer=ans1, day=DAY, year=YEAR, part=2)
