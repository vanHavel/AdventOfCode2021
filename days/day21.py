import copy
import functools

from aocd import get_data, submit

DAY = 21
YEAR = 2021


def part1(data: str) -> str:
    lines = data.splitlines()
    start1 = int(lines[0][-1])
    start2 = int(lines[1][-1])
    positions = [start1-1, start2-1]
    scores = [0, 0]
    done = False
    die = 1
    turns = 0
    while not done:
        for player in range(2):
            rolled = 0
            for roll in range(3):
                rolled += die
                die += 1
                if die == 101:
                    die = 1
            positions[player] += rolled
            positions[player] %= 10
            scores[player] += positions[player] + 1
            turns += 1
            if scores[player] >= 1000:
                done = True
                break
    ans = 3 * turns * scores[1-player]
    return str(ans)


def part2(data: str) -> str:
    lines = data.splitlines()
    start1 = int(lines[0][-1])
    start2 = int(lines[1][-1])
    positions = (start1-1, start2-1)
    scores = (0, 0)
    wins, losses = outcomes(0, scores, positions)
    ans = max(wins, losses)
    return str(ans)


@functools.lru_cache(maxsize=None)
def outcomes(player: int, scores: tuple, positions: tuple) -> tuple:
    if scores[1-player] >= 21:
        return 0, 1
    wins, losses = 0, 0
    for roll1 in range(3):
        for roll2 in range(3):
            for roll3 in range(3):
                rolled = roll1 + roll2 + roll3 + 3
                new_positions = list(copy.copy(positions))
                new_positions[player] += rolled
                new_positions[player] %= 10
                new_scores = list(copy.copy(scores))
                new_scores[player] += new_positions[player] + 1
                other, mine = outcomes(1-player, tuple(new_scores), tuple(new_positions))
                wins += mine
                losses += other
    return wins, losses



if __name__ == '__main__':
    input_data = get_data(day=DAY, year=YEAR)
    ans1 = part1(input_data)
    #submit(answer=ans1, day=DAY, year=YEAR, part=1)
    ans2 = part2(input_data)
    submit(answer=ans2, day=DAY, year=YEAR, part=2)
