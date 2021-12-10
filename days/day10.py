from aocd import get_data, submit

DAY = 10
YEAR = 2021


def part1(data: str) -> str:
    open = "({[<"
    close = ")}]>"
    ans = 0
    score = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    lines = data.splitlines()
    for line in lines:
        stack = []
        for char in line:
            if char in open:
                stack.append(char)
            else:
                top = stack[-1]
                stack.pop()
                if open.index(top) != close.index(char):
                    ans += score[char]
                    break
    return str(ans)


def part2(data: str) -> str:
    open = "([{<"
    close = ")]}>"
    scores = []
    lines = data.splitlines()
    for line in lines:
        ok = True
        stack = []
        for char in line:
            if char in open:
                stack.append(char)
            else:
                top = stack[-1]
                stack.pop()
                if open.index(top) != close.index(char):
                    ok = False
                    break
        if ok:
            score = 0
            while stack:
                score *= 5
                top = stack[-1]
                score += open.index(top) + 1
                stack.pop()
            scores.append(score)
    scores = sorted(scores)
    n = len(scores)
    ans = scores[n // 2]
    return str(ans)


if __name__ == '__main__':
    input_data = get_data(day=DAY, year=YEAR)
    ans1 = part1(input_data)
    #submit(answer=ans1, day=DAY, year=YEAR, part=1)
    ans2 = part2(input_data)
    submit(answer=ans2, day=DAY, year=YEAR, part=2)
