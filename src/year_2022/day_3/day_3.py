from typing import List


def get_item_priority(item: str) -> int:
    """
    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.
    """
    return ord(item) - (64 - 26) if item.isupper() else ord(item) - 96


def compute_part1(lines: List[str]) -> int:
    score = 0
    for line in lines:
        common_item = set(line[:len(line) // 2]) & set(line[len(line) // 2:])
        score += get_item_priority(common_item.pop())
    return score


def compute_part2(lines: List[str]) -> int:
    score = 0
    while lines:
        print(f"line: {lines[0]}")
        for char in lines[0]:
            if (char in lines[1] and char in lines[2]):
                print(
                    f"found {char} in all 3: {lines[0]} {lines[1]} {lines[2]}")
                score += get_item_priority(char)
                break
        lines.pop(0)
        lines.pop(0)
        lines.pop(0)

    return score


def main(lines: List[str]):
    print(f"Part 1: {compute_part1(lines)}")
    print(f"Part 2: {compute_part2(lines)}")
