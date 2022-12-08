from typing import List


def number_character_before_unique_set(set_lentgh: int, data_stream: str) -> int:
    for index, _ in enumerate(data_stream):
        if len(set(data_stream[index:index+set_lentgh])) == len(data_stream[index:index+set_lentgh]):
            return index + set_lentgh

def compute_part1(lines: List[str]) -> int:
    return number_character_before_unique_set(4, lines[0])


def compute_part2(lines: List[str]) -> int:
    return number_character_before_unique_set(14, lines[0])


def main(lines: List[str]):
    print(f"Part 1: {compute_part1(lines)}")
    print(f"Part 2: {compute_part2(lines)}")
