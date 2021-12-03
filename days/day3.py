import copy

from aocd import get_data, submit

DAY = 3
YEAR = 2021


def part1(data: str) -> str:
    lines = data.splitlines()
    reps = [list(l) for l in lines]
    d = len(reps[0])
    ones = [sum([1 if l[i] == '1' else 0  for l in reps]) for i in range(d)]
    zeros = [sum([0 if l[i] == '1' else 1 for l in reps]) for i in range(d)]
    bin = 1
    res = 0
    for i in range(d-1, -1, -1):
        if ones[i] > zeros[i]:
            res += bin
        bin *= 2
    return str(res * (bin - 1 - res))


def part2(data: str) -> str:
    lines = data.splitlines()
    reps = [list(l) for l in lines]
    d = len(reps[0])
    gamma = 0
    bin = int(2 ** (d - 1))
    greps = copy.deepcopy(reps)
    for i in range(d):
        ones = sum([1 if l[i] == '1' else 0 for l in greps])
        zeros = sum([0 if l[i] == '1' else 1 for l in greps])
        if len(greps) == 1:
            gamma += bin * int(greps[0][i])
        elif ones >= zeros:
            gamma += bin
            greps = [l for l in greps if l[i] == '1']
        else:
            greps = [l for l in greps if l[i] == '0']
        bin //= 2
    greps = copy.deepcopy(reps)
    eps = 0
    bin = int(2 ** (d - 1))
    for i in range(d):
        ones = sum([1 if l[i] == '1' else 0 for l in greps])
        zeros = sum([0 if l[i] == '1' else 1 for l in greps])
        if len(greps) == 1:
            eps += bin * int(greps[0][i])
        elif zeros > ones:
            eps += bin
            greps = [l for l in greps if l[i] == '1']
        else:
            greps = [l for l in greps if l[i] == '0']
        bin //= 2
    return str(gamma * eps)


if __name__ == '__main__':
    input_data = get_data(day=DAY, year=YEAR)
    ans1 = part1(input_data)
    submit(answer=ans1, day=DAY, year=YEAR, part=1)
    ans2 = part2(input_data)
    submit(answer=ans2, day=DAY, year=YEAR, part=2)
