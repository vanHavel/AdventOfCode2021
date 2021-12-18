import ast
import copy
from dataclasses import dataclass
from typing import Optional, Union

from aocd import get_data, submit

DAY = 18
YEAR = 2021


@dataclass
class Tree:
    parent: Optional['Tree']


@dataclass
class Leaf(Tree):
    val: int


@dataclass
class Node(Tree):
    left: Tree
    right: Tree


def add(a: Tree, b: Tree) -> Tree:
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    node = Node(left=a, right=b, parent=None)
    node.left.parent = node
    node.right.parent = node
    reduce(node)
    return node


def find(a: Tree, depth: int, explode: bool) -> Optional[Tree]:
    if isinstance(a, Leaf):
        if not explode and a.val >= 10:
            return a
        else:
            return None
    elif isinstance(a, Node):
        if explode and depth == 4:
            assert isinstance(a.left, Leaf)
            assert isinstance(a.right, Leaf)
            return a
        else:
            l = find(a.left, depth + 1, explode)
            if l:
                return l
            return find(a.right, depth + 1, explode)


def reduce(a: Tree) -> None:
    change = True
    while change:
        change = False
        if to_explode := find(a, 0, True):
            explode(to_explode)
            change = True
        elif to_split := find(a, 0, False):
            split(to_split)
            change = True


def explode(a: Tree) -> Tree:
    assert isinstance(a, Node)
    assert isinstance(a.left, Leaf)
    assert isinstance(a.right, Leaf)
    left = find_left(a)
    if left:
        left.val += a.left.val
    right = find_right(a)
    if right:
        right.val += a.right.val
    if a is a.parent.left:
        a.parent.left = Leaf(val=0, parent=a.parent)
    else:
        a.parent.right = Leaf(val=0, parent=a.parent)


def find_left(a: Tree) -> Optional[Tree]:
    if a.parent is None:
        return None
    if a is a.parent.right:
        cand = a.parent.left
        while isinstance(cand, Node):
            cand = cand.right
        return cand
    else:
        return find_left(a.parent)


def find_right(a: Tree) -> Optional[Tree]:
    if a.parent is None:
        return None
    if a is a.parent.left:
        cand = a.parent.right
        while isinstance(cand, Node):
            cand = cand.left
        return cand
    else:
        return find_right(a.parent)


def split(a: Tree) -> None:
    par: Node = a.parent
    nl = a.val // 2
    nr = (a.val+1) // 2
    np = Node(left=Leaf(val=nl, parent=None), right=Leaf(val=nr, parent=None), parent=par)
    np.left.parent = np
    np.right.parent = np
    if par.left is a:
        par.left = np
    else:
        par.right = np


def parse(thing: Union[int, list]) -> Tree:
    if isinstance(thing, int):
        return Leaf(val=thing, parent=None)
    elif isinstance(thing, list):
        return Node(left=parse(thing[0]), right=parse(thing[1]), parent=None)


def set_parents(a: Tree) -> Tree:
    if isinstance(a, Node):
        a.left.parent = a
        a.right.parent = a
        set_parents(a.left)
        set_parents(a.right)
    return a


def magnitude(a: Tree) -> int:
    if isinstance(a, Leaf):
        return a.val
    else:
        assert isinstance(a, Node)
        return 3 * magnitude(a.left) + 2 * magnitude(a.right)


def part1(data: str) -> str:
    lines = data.splitlines()
    trees = [set_parents(parse(ast.literal_eval(line))) for line in lines]
    res = trees[0]
    for tree in trees[1:]:
        res = add(res, tree)
    ans = magnitude(res)
    return str(ans)


def part2(data: str) -> str:
    lines = data.splitlines()
    trees = [set_parents(parse(ast.literal_eval(line))) for line in lines]
    best = 0
    for a in trees:
        for b in trees:
            if a is b:
                continue
            cand = magnitude(add(a, b))
            best = max(best, cand)
            cand = magnitude(add(b, a))
            best = max(best, cand)
    return str(best)


if __name__ == '__main__':
    input_data = get_data(day=DAY, year=YEAR)
    ans1 = part1(input_data)
    #submit(answer=ans1, day=DAY, year=YEAR, part=1)
    ans2 = part2(input_data)
    submit(answer=ans2, day=DAY, year=YEAR, part=2)
