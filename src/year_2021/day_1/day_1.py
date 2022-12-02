"""
Day 1
"""

from typing import List


def compute_increase_number(lines: List[int]):
    count = 0
    for i, value in enumerate(lines):
        if i == 0:
            continue

        if value > lines[i-1]:
            count += 1

    return count

def compute_increase_number_by_trio(lines: List[int]):
    count = 0
    for i, _ in enumerate(lines):
        if i == 0:
            continue
        if len(lines) - i < 3:
            break

        if sum(lines[i:i+3]) > sum(lines[i-1:i-1+3]):
            count += 1

    return count


def main(lines: List[str]):
    numbers = [int(line) for line in lines]

    print(f"Part 1: {compute_increase_number(numbers)}")
    print(f"Part 2: {compute_increase_number_by_trio(numbers)}")
