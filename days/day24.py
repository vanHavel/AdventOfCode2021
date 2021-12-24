from aocd import get_data, submit
import string

DAY = 24
YEAR = 2021


def part(data: str, small: bool) -> str:
    lines = data.splitlines()
    stuffs = []
    for i in range(14):
        chunk = list(map(lambda s: "".join(list(filter(lambda c: c in string.digits + "-1", s))), lines[:18]))
        stuff = {
            'div': int(chunk[4]),
            'n1': int(chunk[5]),
            'n2': int(chunk[15])
        }
        stuffs.append(stuff)
        lines = lines[18:]
    if small:
        rng = range(9999999)
    else:
        rng = range(9999999, -1, -1)
    for input in rng:
        z = 0
        ans = ""
        dindex = 0
        for index in range(14):
            stuff = stuffs[index]
            if stuff['div'] == 1:
                digit = str(input).zfill(7)[dindex]
                z = section(w=int(digit), z=z, **stuffs[index])
                ans += digit
                dindex += 1
            else:
                fixed = z % 26 + stuff['n1']
                if fixed > 9 or fixed < 0:
                    z = "wrong"
                    break
                z = section(w=fixed, z=z, **stuffs[index])
                ans += str(fixed)
        if z == 0 and "0" not in ans:
            return ans


def section(w: int, div: int, n1: int, n2: int, z: int) -> int:
    x = 1 if ((z % 26) + n1) != w else 0
    y1 = 25 * x + 1
    y2 = (w + n2) * x
    z = (z // div) * y1 + y2
    return z


if __name__ == '__main__':
    input_data = get_data(day=DAY, year=YEAR)
    ans1 = part(input_data, False)
    print(ans1)
    #submit(answer=ans1, day=DAY, year=YEAR, part=1)
    ans2 = part(input_data, True)
    print(ans2)
    #submit(answer=ans2, day=DAY, year=YEAR, part=2)
