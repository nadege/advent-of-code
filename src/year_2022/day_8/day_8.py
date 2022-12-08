import math
from typing import List


def is_tree_visible(tree_map: List[str], x: int, y: int) -> bool:
    if (x == 0 or y == 0 or x == (len(tree_map[0])-1) or y == (len(tree_map)-1)):
        return True

    current_tree = tree_map[y][x]
    visibility = {
        'west': True,
        'east': True,
        'north': True,
        'south': True,
    }
    # West
    for tree in tree_map[y][:x]:
        if tree >= current_tree:
            visibility['west'] = False
            break
    # East
    for tree in tree_map[y][x+1:]:
        if tree >= current_tree:
            visibility['east'] = False
            break
    # North
    for tree_line in tree_map[:y]:
        if tree_line[x] >= current_tree:
            visibility['north'] = False
            break
    # South
    for tree_line in tree_map[y+1:]:
        if tree_line[x] >= current_tree:
            visibility['south'] = False
            break

    return any(visibility.values())


def compute_part1(lines: List[str]) -> int:
    return len([tree for y, line in enumerate(lines) for x, tree in enumerate(line) if is_tree_visible(lines, x, y)])


def compute_scenic_score(tree_map: List[str], x: int, y: int) -> bool:
    if (x == 0 or y == 0 or x == (len(tree_map[0])-1) or y == (len(tree_map)-1)):
        return 0

    current_tree = tree_map[y][x]
    # initialise with highest possible visiblity
    visibility = {
        'west': x,
        'east': len(tree_map[0]) - x - 1,
        'north': y,
        'south': len(tree_map) - y - 1,
    }

    # Search for blockers that reduce visibility
    # West
    for index, tree in enumerate(reversed(tree_map[y][:x])):
        if tree >= current_tree:
            visibility['west'] = index + 1
            break
    # East
    for index, tree in enumerate(tree_map[y][x+1:]):
        if tree >= current_tree:
            visibility['east'] = index + 1
            break
    # North
    for index, tree_line in enumerate(reversed(tree_map[:y])):
        if tree_line[x] >= current_tree:
            visibility['north'] = index + 1
            break
    # South
    for index, tree_line in enumerate(tree_map[y+1:]):
        if tree_line[x] >= current_tree:
            visibility['south'] = index + 1
            break

    return math.prod(visibility.values())


def compute_part2(lines: List[str]) -> int:
    return max([compute_scenic_score(lines, x, y) for y, line in enumerate(lines) for x, _ in enumerate(line)])


def main(lines: List[str]):
    print(f"Part 1: {compute_part1(lines)}")
    print(f"Part 2: {compute_part2(lines)}")
