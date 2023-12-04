import math
from enum import Enum


class Colours(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"

game_cubes = {
    Colours.RED: 12,
    Colours.GREEN: 13,
    Colours.BLUE: 14,
}

def compute_part1(lines: list[str]) -> int:
    score = 0

    def is_set_possible(game: str) -> bool:
        
        def is_draw_possible(draw: str) -> bool:
            return all( int(draw.split(colour.value)[0].strip()) <= game_cubes[colour] for colour in Colours if colour.value in draw)
        
        return all(is_draw_possible(draw) for draw in game.split(","))


    for index, line in enumerate(lines):
        game_index = index + 1
        games = line.split(":")[1]
        if all(is_set_possible(cubes_set) for cubes_set in games.split(";")):
            score += game_index              
        
    return score


def compute_part2(lines: list[str]) -> int:
    score = 0

    for game in lines:
        # Get minimum set
        
        cube_sets = game.split(":")[1].split(";")

        minimum_set = [max([int(draw.split(colour.value)[0].strip()) for cube_set in cube_sets for draw in cube_set.split(',') if colour.value in draw]) for colour in Colours]

        # Power of minimim set
        power = math.prod(minimum_set)

        # Update score
        score += power

    return score


def main(lines: list[str]):
    print(f"Part 1: {compute_part1(lines)}")
    print(f"Part 2: {compute_part2(lines)}")
