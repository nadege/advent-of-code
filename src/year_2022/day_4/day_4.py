from typing import List, Tuple


def is_full_overlap(boudaries: List[int]) -> bool:
    a = boudaries[:2]
    b = boudaries[2:]
    return a[0] <= b[0] and a[1] >= b[1] or b[0] <= a[0] and b[1] >= a[1]

def compute_part1(lines: List[str]) -> int:
    score = 0
    for line in lines:
        if is_full_overlap([int(boundary) for elf in line.split(',') for boundary in elf.split('-')]):
            score += 1
    return score


def is_overlap(boudaries: List[int]) -> bool:
    a = boudaries[:2]
    b = boudaries[2:]
    return (a[0] <= b[0] and a[1] >= b[0]) or (b[0] <= a[0] and b[1] >= a[0])


def compute_part2(lines: List[str]) -> int:
    score = 0
    for line in lines:
        if is_overlap([int(boundary) for elf in line.split(',') for boundary in elf.split('-')]):
            score += 1
    return score


def main(lines: List[str]):
    print(f"Part 1: {compute_part1(lines)}")
    print(f"Part 2: {compute_part2(lines)}")
