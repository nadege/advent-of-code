from enum import Enum
from typing import List


class OpponentMoves(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"

class PlayerMoves(Enum):
    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"

play_result = {
    PlayerMoves.ROCK.value: {
        OpponentMoves.ROCK.value: 3,
        OpponentMoves.PAPER.value: 0,
        OpponentMoves.SCISSORS.value: 6,
    },
    PlayerMoves.PAPER.value: {
        OpponentMoves.ROCK.value: 6,
        OpponentMoves.PAPER.value: 3,
        OpponentMoves.SCISSORS.value: 0,
    },
    PlayerMoves.SCISSORS.value: {
        OpponentMoves.ROCK.value: 0,
        OpponentMoves.PAPER.value: 6,
        OpponentMoves.SCISSORS.value: 3,   
    }       
}

move_result = {
    PlayerMoves.ROCK.value: 1,
    PlayerMoves.PAPER.value: 2,
    PlayerMoves.SCISSORS.value: 3,
}

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
expected_results = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}


def get_round_result_for_player(player_move: str, opponent_move: str) -> bool:
    return play_result[player_move][opponent_move] + move_result[player_move]


def compute_score_part1(lines: List[str]) -> int:
    score = 0
    for round in lines:
        score += get_round_result_for_player(round[2], round[0])
    return score

def get_player_move(opponent_move: str, expected_result) -> str:
    for move, results in play_result.items():
        if results[opponent_move] == expected_result:
            return move


def compute_score_part2(lines: List[str]) -> int:
    score = 0
    for game_round in lines:
        score += get_round_result_for_player(get_player_move(game_round[0], expected_results[game_round[2]]), game_round[0])
    return score


def main(lines: List[str]):
    print(f"Part 1: {compute_score_part1(lines)}")
    print(f"Part 1: {compute_score_part2(lines)}")
