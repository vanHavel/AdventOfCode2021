import itertools

from aocd import get_data, submit

DAY = 8
YEAR = 2021

def part1(data: str) -> str:
    lines = data.splitlines()
    ans = 0
    for line in lines:
        left, right = line.split('|')
        segments = left.split(' ')
        code = right.split(' ')
        for item in code:
            if len(item) in [2, 3, 4, 7]:
                ans += 1
    return str(ans)


def part2(data: str) -> str:
    lines = data.splitlines()
    valids = [set("abcefg"), set("cf"), set("acdeg"), set("acdfg"), set("bcdf"), set("abdfg"), set("abdefg"), set("acf"), set("abcdefg"), set("abcdfg")]
    ans = 0
    for line in lines:
        left, right = line.split('|')
        segments = left.strip().split(' ')
        code = right.strip().split(' ')
        for perm in itertools.permutations("abcdefg"):
            mapping = {"abcdefg"[i]: perm[i] for i in range(7)}
            ok = True
            for index, segment in enumerate(segments):
                mapped = set()
                for char in segment:
                    mapped.add(mapping[char])
                if mapped not in valids:
                    ok = False
                    break
            if ok:
                decoded = 0
                for segment in code:
                    decoded *= 10
                    mapped = set()
                    for char in segment:
                        mapped.add(mapping[char])
                    digit = valids.index(mapped)
                    decoded += digit
                ans += decoded
                break
    return str(ans)


if __name__ == '__main__':
    input_data = get_data(day=DAY, year=YEAR)
    ans1 = part1(input_data)
    #submit(answer=ans1, day=DAY, year=YEAR, part=1)
    ans2 = part2(input_data)
    submit(answer=ans2, day=DAY, year=YEAR, part=2)
