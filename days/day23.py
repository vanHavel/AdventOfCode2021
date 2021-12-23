import copy
from dataclasses import dataclass

from aocd import get_data, submit

from util.astar import AStar

DAY = 23
YEAR = 2021


@dataclass
class State:
    rooms: tuple
    hallway: tuple # 11, 2 = A, 4 = B, 6 = C, 8 = D
    def __hash__(self):
        return hash((self.rooms, self.hallway))


def h(s: State):
    return 0

def succ(s: State):
    goals = [2, 4, 6, 8]
    costs = [1, 10, 100, 1000]
    succs = []
    # move in
    for index, field in enumerate(s.hallway):
        if field != -1:
            if (index <= goals[field] and all(s.hallway[i] == -1 for i in range(index+1, goals[field]+1))) \
                    or (index > goals[field] and all(s.hallway[i] == -1 for i in range(index-1, goals[field]-1, -1))):
                newhall = list(s.hallway)
                newhall[index] = -1
                target_room = s.rooms[field]
                for target_pos in range(len(target_room)):
                    if target_room[target_pos] == -1 \
                            and all(target_room[pos] == -1 for pos in range(target_pos)) \
                            and all(target_room[pos] == field for pos in range(target_pos+1, len(target_room))):
                        newrooms = list(s.rooms)
                        newroom = list(target_room)
                        newroom[target_pos] = field
                        newrooms[field] = tuple(newroom)
                        dist = abs(index - goals[field]) + 1 + target_pos
                        succs.append((costs[field]*dist, State(hallway=tuple(newhall), rooms=tuple(newrooms))))
    # move out
    for index, room in enumerate(s.rooms):
        if s.hallway[goals[index]] != -1:
            continue
        hmin = goals[index]
        hmax = goals[index]
        while hmin > 0 and s.hallway[hmin-1] == -1:
            hmin -= 1
        while hmax < 10 and s.hallway[hmax+1] == -1:
            hmax += 1
        for target in range(hmin, hmax+1):
            if target in goals:
                continue
            roomindex = 0
            while roomindex < len(room) and room[roomindex] == -1:
                roomindex += 1
            if roomindex != len(room) and any(room[pos] != index for pos in range(roomindex, len(room))):
                guy = room[roomindex]
                newhall = list(s.hallway)
                newhall[target] = guy
                newrooms = list(s.rooms)
                newroom = list(newrooms[index])
                newroom[roomindex] = -1
                newrooms[index] = tuple(newroom)
                dist = abs(target - goals[index]) + 1 + roomindex
                succs.append((costs[guy]*dist, State(hallway=tuple(newhall), rooms=tuple(newrooms))))
    return succs


def part1(data: tuple) -> str:
    empty = tuple([-1 for i in range(11)])
    start = State(rooms=data, hallway=empty)
    finish = State(rooms=tuple([tuple([i for _ in range(len(data[0]))]) for i in range(4)]), hallway=empty)
    ast = AStar(
        goal=lambda s: s == finish,
        succ=succ,
        h=h
    )
    cost, hist = ast.search(start=start)
    print(cost)
    return str(cost)


def part2(data: str) -> str:
    pass


if __name__ == '__main__':
    input_data = ((1, 2), (1, 0), (3, 3), (0, 2))
    ans1 = part1(input_data)
    #submit(answer=ans1, day=DAY, year=YEAR, part=1)
    full_data = ((1, 3, 3, 2), (1, 2, 1, 0), (3, 1, 0, 3), (0, 0, 2, 2))
    ans2 = part1(full_data)
    submit(answer=ans2, day=DAY, year=YEAR, part=2)
