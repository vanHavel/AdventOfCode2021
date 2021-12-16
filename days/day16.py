from dataclasses import dataclass
from typing import List

from aocd import get_data, submit

DAY = 16
YEAR = 2021


class Package:
    pass


@dataclass
class Literal(Package):
    version: int
    type: int
    value: int


@dataclass
class Operator(Package):
    version: int
    type: int
    subs: List[Package]


def parse(binary: str):
    version = int(binary[:3], 2)
    type = int(binary[3:6], 2)
    if type == 4:
        rest = binary[6:]
        more = 1
        value = 0
        while more != 0:
            value *= 16
            group = rest[:5]
            more = int(group[0])
            value += int(group[1:], 2)
            rest = rest[5:]
        return Literal(version, type, value), rest
    else:
        rest = binary[6:]
        len_id = int(binary[6])
        if len_id == 0:
            total = int(binary[7:22], 2)
            seen = 0
            subs = []
            rem = binary[22:]
            while seen < total:
                package, rest = parse(rem)
                seen += len(rem) - len(rest)
                subs.append(package)
                rem = rest
            assert seen == total
            return Operator(version, type, subs), rem
        elif len_id == 1:
            packs = int(binary[7:18], 2)
            print(f'pack op {packs}')
            subs = []
            rest = binary[18:]
            for _ in range(packs):
                package, rest = parse(rest)
                subs.append(package)
            return Operator(version, type, subs), rest
        else:
            raise ValueError("Wrong length id")


def part1(data: Package) -> int:
    if isinstance(data, Literal):
        return data.version
    elif isinstance(data, Operator):
        return data.version + sum(part1(sub) for sub in data.subs)


def part2(data: Package) -> int:
    if isinstance(data, Literal):
        return data.value
    elif isinstance(data, Operator):
        if data.type == 0:
            return sum(part2(sub) for sub in data.subs)
        elif data.type == 1:
            prod = 1
            for sub in data.subs:
                prod *= part2(sub)
            return prod
        elif data.type == 2:
            return min(part2(sub) for sub in data.subs)
        elif data.type == 3:
            return max(part2(sub) for sub in data.subs)
        elif data.type == 5:
            left, right = [part2(sub) for sub in data.subs]
            return int(left > right)
        elif data.type == 6:
            left, right = [part2(sub) for sub in data.subs]
            return int(left < right)
        elif data.type == 7:
            left, right = [part2(sub) for sub in data.subs]
            return int(left == right)
        else:
            raise ValueError("Invalid type")


if __name__ == '__main__':
    data = get_data(day=DAY, year=YEAR)
    hexi = int(data, 16)
    bits = len(data) * 4
    bini = str(bin(hexi))[2:].zfill(bits)
    parsed, rest = parse(bini)
    ans1 = str(part1(parsed))
    #submit(answer=ans1, day=DAY, year=YEAR, part=1)
    ans2 = str(part2(parsed))
    submit(answer=ans2, day=DAY, year=YEAR, part=2)
