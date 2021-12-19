import copy

from aocd import get_data, submit

DAY = 19
YEAR = 2021

# https://stackoverflow.com/questions/16452383/how-to-get-all-24-rotations-of-a-3-dimensional-array
def roll(v): return [v[0],v[2],-v[1]]
def turn(v): return [-v[1],v[0],v[2]]
def sequence (v):
    for cycle in range(2):
        for step in range(3):  # Yield RTTT 3 times
            v = roll(v)
            yield(v)           #    Yield R
            for i in range(3): #    Yield TTT
                v = turn(v)
                yield(v)
        v = roll(turn(roll(v)))  # Do RTR


def part1(data: str) -> str:
    lines = data.splitlines()
    scanners = []
    beac = []
    for line in lines:
        if 'scanner' in line:
            beac = []
        elif line == '':
            scanners.append(beac)
        else:
            xs, ys, zs = list(map(int, line.split(',')))
            beac.append([xs, ys, zs])
    scanners.append(beac)
    positions = [None for s in scanners]
    positions[0] = [0, 0, 0]
    check = [0]
    while check != []:
        next = check.pop()
        for index in range(len(scanners)):
            if index != check and positions[index] is None:
                for rot in range(24):
                    s1 = scanners[next]
                    s2 = copy.deepcopy(scanners[index])
                    for k, point in enumerate(s2):
                        s2[k] = list(sequence(point))[rot]
                    found = False
                    for i1 in range(len(s1)):
                        for i2 in range(len(s2)):
                            if found:
                                continue
                            p1 = s1[i1]
                            p2 = s2[i2]
                            diff = [p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]]
                            match = 0
                            for q2 in s2:
                                moved = [q2[0] - diff[0], q2[1] - diff[1], q2[2] - diff[2]]
                                if moved in s1:
                                    match += 1
                            if match >= 12 and index not in check:
                                checkpos = positions[next]
                                newpos = [checkpos[0] - diff[0], checkpos[1] - diff[1], checkpos[2] - diff[2]]
                                positions[index] = newpos
                                scanners[index] = s2
                                check.append(index)
                                found = True
    beacons = set()
    for index, scanner in enumerate(scanners):
        spos = positions[index]
        for seen in scanner:
            bpos = (spos[0] + seen[0], spos[1] + seen[1], spos[2] + seen[2])
            beacons.add(bpos)
    ans1 = len(beacons)
    best = 0
    for p1 in positions:
        for p2 in positions:
            dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])
            best = max(dist, best)
    return str(ans1), str(best)


if __name__ == '__main__':
    input_data = get_data(day=DAY, year=YEAR)
    ans1, ans2 = part1(input_data)
    #submit(answer=ans1, day=DAY, year=YEAR, part=1)
    submit(answer=ans2, day=DAY, year=YEAR, part=2)

"""
1 -> 0: [-68, 1246, 43]

4 -> 1: [-88, -113, 1104]

2 -> 4: [-168, 1125, -72]
"""