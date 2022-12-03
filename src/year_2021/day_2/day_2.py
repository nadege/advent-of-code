from typing import List

# horizontal, depth
moves = {
    "forward": (1, 0),
    "down": (0, 1),
    "up": (0, -1),
}

def compute_part1(lines: List[str]):
    horizontal = 0
    depth = 0
    for line in lines:
        move, value = line.split(" ")
        horizontal += int(value) * int(moves[move][0])
        depth += int(value) * int(moves[move][1])
    return horizontal * depth

# horizontal, depth
def moves_2(aim: int):
    """
    down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
    It increases your horizontal position by X units.
    It increases your depth by your aim multiplied by X.
    """
    # horizontal, depth, aim
    return {
        "forward": (1, aim, 0),
        "down": (0, 0, 1),
        "up": (0, 0, -1),
    }


def compute_part2(lines: List[str]):
    horizontal = 0
    depth = 0
    aim = 0
    for line in lines:
        move, value = line.split(" ")
        horizontal += int(value) * int(moves_2(aim)[move][0])
        depth += int(value) * int(moves_2(aim)[move][1])
        aim +=int(value) * int(moves_2(aim)[move][2])
    return horizontal * depth


def main(lines: List[str]):
    print(f"Part 1: {compute_part1(lines)}")
    print(f"Part 1: {compute_part2(lines)}")