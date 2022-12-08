"""
Initial setup

[P]     [L]         [T]            
[L]     [M] [G]     [G]     [S]    
[M]     [Q] [W]     [H] [R] [G]    
[N]     [F] [M]     [D] [V] [R] [N]
[W]     [G] [Q] [P] [J] [F] [M] [C]
[V] [H] [B] [F] [H] [M] [B] [H] [B]
[B] [Q] [D] [T] [T] [B] [N] [L] [D]
[H] [M] [N] [Z] [M] [C] [M] [P] [P]
 1   2   3   4   5   6   7   8   9 

"""

from copy import copy
from typing import List


initial_crates = [
    "---",
    "HBVWNMLP",  # 1
    "MQH",   # 2
    "NDBGFQML",   # 3
    "ZTFQMWG",   # 4
    "MTHP",   # 5
    "CBMJDHGT",   # 6
    "MNBFVR",   # 7
    "PLHMRGS",   # 8
    "PDBCN",  # 9
]


def compute_part1(lines: List[str]) -> int:
    """
    move 8 from 3 to 2
    """
    crates = copy(initial_crates)
    
    for move in lines:
        [quantity, from_, to_] = [int(data) for data in move.split(' ') if data.isnumeric()]
        crates[to_] += ''.join(reversed(crates[from_][-quantity:]))
        crates[from_] = crates[from_][:-quantity]

    return ''.join([crate[-1] for crate in crates[1:]])


def compute_part2(lines: List[str]) -> int:
    crates = copy(initial_crates)
    
    for move in lines:
        [quantity, from_, to_] = [int(data) for data in move.split(' ') if data.isnumeric()]
        crates[to_] += crates[from_][-quantity:]
        crates[from_] = crates[from_][:-quantity]

    return ''.join([crate[-1] for crate in crates[1:]])


def main(lines: List[str]):
    print(f"Part 1: {compute_part1(lines)}")
    print(f"Part 2: {compute_part2(lines)}")
