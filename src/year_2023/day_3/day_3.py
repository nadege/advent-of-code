import math
from collections import defaultdict


def find_numbers(line: str) -> list[tuple[int, str]]:
    numbers = []
    current_number_start = None
    current_number_acc = ""
    for index, char in enumerate(line):
        if char.isdigit():
            current_number_acc += char
            current_number_start = current_number_start or index
        else:
            if current_number_start is not None:
                numbers.append((current_number_start, current_number_acc))
                current_number_start = None
                current_number_acc = ""

    if current_number_start is not None:
        numbers.append((current_number_start, current_number_acc))

    return numbers

def is_next_to_symbol(number_index: int, number_str: int, lines: list[str], symbol: str | None = None) -> tuple[int, int] | None:
    number_length = len(number_str)
    for line_index, line in enumerate(lines):
        first_char = number_index-1 if number_index else 0
        last_char = number_index+number_length+1 if number_index+number_length <= len(line) else number_index+number_length
        for char_index, char in enumerate(line[first_char:last_char]):
            if not char.isdigit() and (char == symbol if symbol else char != "."):
                return (line_index, char_index+first_char)

    for line in lines:
        first_char = number_index-1 if number_index else 0
        last_char = number_index+number_length+1 if number_index+number_length <= len(line) else number_index+number_length  

    return None

def compute_part1(lines: list[str]) -> int:
    score = 0

    for line_index, line in enumerate(lines):
        numbers = find_numbers(line)
        first_line = line_index-1 if line_index else 0
        last_line = line_index+1 if line_index < len(lines) else line_index
        print(f"check line {line_index}: lines {first_line} to {last_line}, for numbers {numbers}")
        
        # print lines
        for line in lines[first_line:last_line+1]:
            print(f"Line: {line}")

        is_next = []
        is_not_next = []
        for (number_index, number_str) in numbers:
            if is_next_to_symbol(number_index, number_str, lines[first_line:last_line+1]):
                score += int(number_str)
                is_next.append(number_str)
            else:
                is_not_next.append(number_str)

        print(f"next: {is_next}, not next: {is_not_next}")

    return score


def compute_part2(lines: list[str]) -> int:
    key_parts = defaultdict(list)
    for line_index, line in enumerate(lines):
        numbers = find_numbers(line)
        first_line = line_index-1 if line_index else 0
        last_line = line_index+1 if line_index < len(lines) else line_index
        print(f"check line {line_index}: lines {first_line} to {last_line}, for numbers {numbers}")
        
        # print lines
        for line in lines[first_line:last_line+1]:
            print(f"Line: {line}")

        for (number_index, number_str) in numbers:
            if position := is_next_to_symbol(number_index, number_str, lines[first_line:last_line+1], symbol="*"):
                position = (position[0]+first_line, position[1])
                print(f"Found * at {position} for {number_str}")
                key_parts[position].append(int(number_str))
                
    return sum(math.prod(parts) for parts in key_parts.values() if len(parts) == 2 )


def main(lines: list[str]):
    print(f"Part 1: {compute_part1(lines)}")
    print(f"Part 2: {compute_part2(lines)}")
