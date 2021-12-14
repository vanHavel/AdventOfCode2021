from collections import Counter

from aocd import get_data, submit

DAY = 14
YEAR = 2021


def part(data: str, steps: int) -> str:
    lines = data.splitlines()
    start = lines[0]
    ll = start[-1]
    rest = lines[2:]
    rules = dict()
    for line in rest:
        left, right = line.split("->")
        rules[left.strip()] = right.strip()

    pairs = Counter()
    for i in range(len(start)-1):
        pairs[start[i:i+2]] += 1
    for step in range(steps):
        new = Counter()
        for pair, count in pairs.items():
            first = pair[0]
            second = pair[1]
            mapped = rules[pair]
            new[first + mapped] += count
            new[mapped + second] += count
        pairs = new

    letters = Counter()
    for pair, count in pairs.items():
        letter = pair[0]
        letters[letter] += count
    letters[ll] += 1
    vals = letters.values()
    res = max(vals) - min(vals)
    return str(res)


if __name__ == '__main__':
    input_data = get_data(day=DAY, year=YEAR)
    ans1 = part(input_data, 10)
    submit(answer=ans1, day=DAY, year=YEAR, part=1)
    ans2 = part(input_data, 40)
    #submit(answer=ans2, day=DAY, year=YEAR, part=2)
