from pprint import pprint
from typing import List


def compute_part1(lines: List[str]):
    signal_strengh = []
    x_register = 1
    cycle_count = 1
    for line in lines:
        splits = line.split(' ')

        if splits[0] == 'noop':
            cycle_count += 1
        elif splits[0] == 'addx':
            cycle_count += 1

        if cycle_count in [20, 60, 100, 140, 180, 220]:
            signal_strengh.append(x_register * cycle_count)

        if splits[0] == 'addx':
            cycle_count += 1
            x_register += int(splits[1])

        if cycle_count in [20, 60, 100, 140, 180, 220]:
            signal_strengh.append(x_register * cycle_count)

    return sum(signal_strengh)


def compute_part2(lines: List[str]):
    x_register = 1
    cycle_count = 1
    screen = [['.'] * 40 for i in range(7)]

    def get_screen_coord(index: int):
        offset_index = index - 1
        return (offset_index % 40, offset_index // 40)

    def is_sprite_on_cursor(screen_coord, x_register):
        return abs(x_register - screen_coord[0]) <= 1

    screen_coord = get_screen_coord(cycle_count)
    screen[screen_coord[1]][screen_coord[0]] = '#' if is_sprite_on_cursor(screen_coord, x_register) else '.'
    for line in lines:
        splits = line.split(' ')

        if splits[0] == 'noop':
            cycle_count += 1
        elif splits[0] == 'addx':
            cycle_count += 1

        screen_coord = get_screen_coord(cycle_count)
        screen[screen_coord[1]][screen_coord[0]] = '#' if is_sprite_on_cursor(screen_coord, x_register) else '.'

        if splits[0] == 'addx':
            cycle_count += 1
            x_register += int(splits[1])
            screen_coord = get_screen_coord(cycle_count)
            screen[screen_coord[1]][screen_coord[0]] = '#' if is_sprite_on_cursor(screen_coord, x_register) else '.'

    print(f"Cycle count: {cycle_count}")
    return screen


def main(lines: List[str]):
    print(f"Part 1: {compute_part1(lines)}")
    pprint("Part 2:")
    pprint([''.join(line) for line in compute_part2(lines)])
