"""
Day 1, who got the more calories?
"""

from typing import List
from helpers import helpers


def compute_snacks(lines: List[str]):
    elves_stash = []
    current_stash = 0
    for line in lines:
        if line == "":
            elves_stash.append(current_stash)
            current_stash = 0
            continue

        current_stash += int(line)

    return elves_stash

def main(lines: List[str]):
    elves_snacks = compute_snacks(lines)
    elves_snacks.sort(reverse=True)

    print(f"Part 1: {elves_snacks[0]}")
    print(f"Part 2: {sum(elves_snacks[0:3])}")
