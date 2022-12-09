import math
from typing import List, Tuple


def does_node_need_to_move(head_position: Tuple[int, int], tail_position: Tuple[int, int]) -> bool:
    # returns true if euclidian distance is greater than math.sqrt(2)
    return math.sqrt((head_position[0] - tail_position[0]) ** 2 + (head_position[1] - tail_position[1]) ** 2) > math.sqrt(2)

def get_node_direction(head_position: Tuple[int, int], tail_position: Tuple[int, int]) -> str:
    # on the same line
    if head_position[1] == tail_position[1]:
        tail_direction = 'R' if head_position[0] > tail_position[0] else 'L'
    # on the same column
    elif head_position[0] == tail_position[0]:
        tail_direction = 'D' if head_position[1] > tail_position[1] else 'U'
    else:
        # move diagonally
        if head_position[1] > tail_position[1]:
            if head_position[0] > tail_position[0]:
                tail_direction = 'DR'
            else:
                tail_direction = 'DL'
        else:
            if head_position[0] > tail_position[0]:
                tail_direction = 'UR'
            else:
                tail_direction = 'UL'  
    return tail_direction

def move(initial_position, direction):
    if direction == 'U':
        return (initial_position[0], initial_position[1] - 1)
    elif direction == 'D':
        return (initial_position[0], initial_position[1] + 1)
    elif direction == 'R':
        return (initial_position[0] + 1, initial_position[1])
    elif direction == 'L':
        return (initial_position[0] - 1, initial_position[1])
    elif len(direction) == 2:
        res = move(initial_position, direction[0])
        return move(res, direction[1])
    else:
        raise ValueError(f"Unknown direction {direction}")

def compute_part1(lines: List[str]) -> int:
    initial_position = 0, 0
    visited_places = set()
    visited_places.add(initial_position)
    head_position = (0, 0)
    tail_position = (0, 0)

    for line in lines:
        [direction, distance] = line.split(' ')

        for _ in range(int(distance)):
            head_position = move(head_position, direction)
            if does_node_need_to_move(head_position, tail_position):
                tail_direction = get_node_direction(head_position, tail_position)
                tail_position = move(tail_position, tail_direction)
                visited_places.add(tail_position)

    return len(visited_places)


def compute_part2(lines: List[str]) -> int:
    initial_position = 0, 0
    visited_places = set()
    visited_places.add(initial_position)
    head_position = (0, 0)
    nodes_positions = [(0, 0)] * 9

    for line in lines:
        [direction, distance] = line.split(' ')

        for _ in range(int(distance)):
            head_position = move(head_position, direction)
            for index, node in enumerate(nodes_positions):
                head = head_position if index == 0 else nodes_positions[index-1]
                if does_node_need_to_move(head_position if index == 0 else nodes_positions[index-1], node):
                    move_direction = get_node_direction(head, node)
                    nodes_positions[index] = move(node, move_direction)
                    
                    
            visited_places.add(nodes_positions[-1])

    return len(visited_places)


def main(lines: List[str]):

    test_input = [
        "R 4",
        "U 4",
        "L 3",
        "D 1",
        "R 4",
        "D 1",
        "L 5",
        "R 2",
    ]

    print(f"Part 1: {compute_part1(lines)}")
    print(f"Part 1: {compute_part1(test_input)}")
    print(f"Part 2: {compute_part2(lines)}")
