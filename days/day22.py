import copy

from aocd import get_data, submit

DAY = 22
YEAR = 2021


def parse(data: str) -> list:
    lines = data.splitlines()
    ops = []
    for line in lines:
        actionst, rest = line.split()
        action = "on" in actionst
        coords = rest.strip().split(",")
        ranges = []
        for coord in coords:
            begs, ends = coord[2:].strip().split("..")
            beg, end = int(begs.strip()), int(ends.strip())
            ranges.append((beg, end))
        ops.append((action, tuple(ranges)))
    return ops


def part1(data: str) -> str:
    ops = parse(data)
    turned = set()

    def clamp(mi, ma):
        if mi > 50 or ma < -50:
            return None, None
        return max(-50, mi), min(50, ma)
    for action, ranges in ops:
        xmin, xmax = clamp(*ranges[0])
        ymin, ymax = clamp(*ranges[1])
        zmin, zmax = clamp(*ranges[2])
        if xmin is not None and ymin is not None and zmin is not None:
            for x in range(xmin, xmax+1):
                for y in range(ymin, ymax+1):
                    for z in range(zmin, zmax+1):
                        if action:
                            turned.add((x, y, z))
                        elif (x, y, z) in turned:
                            turned.remove((x, y, z))
    return str(len(turned))


def part2(data: str) -> str:
    ops = parse(data)
    _, ranges = ops[0]
    turned = set()
    turned.add(ranges)
    for action, ranges in ops[1:]:
        assert len(turned) != 0

        for cuboid in copy.deepcopy(turned):
            intersection = intersect(cuboid, ranges)
            if intersection:
                turned.remove(cuboid)
                externals = outof(ranges, cuboid)
                for external in externals:
                    turned.add(external)
        if action:
            turned.add(ranges)
    ans = 0
    for cuboid in turned:
        ans += size(cuboid)
    return str(ans)


def outof(c1, c2):
    ext_ranges = [[], [], []]
    for index, (c1r, c2r) in enumerate(zip(c1, c2)):
        c1min, c1max = c1r
        c2min, c2max = c2r
        if c2min < c1min:
            ext_ranges[index].append((c2min, min(c2max, c1min-1)))
        if c2max > c1max:
            ext_ranges[index].append((max(c2min, c1max+1), c2max))
    res = []
    fxr, fyr, fzr = c2
    sxr, syr, syz = c1
    for xr in ext_ranges[0]:
        res.append((xr, fyr, fzr))
    for yr in ext_ranges[1]:
        res.append((intersect_range(fxr, sxr), yr, fzr))
    for zr in ext_ranges[2]:
        res.append((intersect_range(fxr, sxr), intersect_range(fyr, syr), zr))
    return res


def intersect(c1, c2):
    intersection = []
    for c1r, c2r in zip(c1, c2):
        its = intersect_range(c1r, c2r)
        if its is None:
            return None
        intersection.append(its)
    return intersection


def intersect_range(r1, r2):
    mi = max(r1[0], r2[0])
    ma = min(r1[1], r2[1])
    if mi > ma:
        return None
    return mi, ma


def size(c):
    prod = 1
    for r in c:
        diff = r[1] - r[0] + 1
        prod *= diff
    return prod


if __name__ == '__main__':
    input_data = get_data(day=DAY, year=YEAR)
    ans1 = part1(input_data)
    #submit(answer=ans1, day=DAY, year=YEAR, part=1)
    ans2 = part2(input_data)
    submit(answer=ans2, day=DAY, year=YEAR, part=2)
