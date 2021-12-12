from collections import defaultdict

from aocd import get_data, submit

DAY = 12
YEAR = 2021


def part(data: str) -> str:
    lines = data.splitlines()
    adj = defaultdict(list)
    for line in lines:
        left, right = line.split('-')
        adj[left].append(right)
        adj[right].append(left)
    ans1 = backtrack(adj, ['start'], False)
    ans2 = backtrack(adj, ['start'], True)
    return str(ans1), str(ans2)


def backtrack(adj, history, free):
    last = history[-1]
    if last == 'end':
        return 1
    ans = 0
    for next in adj[last]:
        if next not in history or next.lower() != next or (free and next != 'start'):
            change = False
            if next in history and next.lower() == next:
                free = False
                change = True
            history.append(next)
            ans += backtrack(adj, history, free)
            if change:
                free = True
            history.pop()
    return ans


if __name__ == '__main__':
    input_data = get_data(day=DAY, year=YEAR)
    ans1, ans2 = part(input_data)
    #submit(answer=ans1, day=DAY, year=YEAR, part=1)
    submit(answer=ans2, day=DAY, year=YEAR, part=2)
