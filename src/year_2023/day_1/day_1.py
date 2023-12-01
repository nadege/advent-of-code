from typing import List


def compute_part1(lines: List[str]) -> int:
    score = 0

    for line in lines:
        digits = [digit for digit in line if digit.isdigit()]
        score += int(digits[0] + digits[-1])

    return score


def compute_part2(lines: List[str]) -> int:
    digit_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    score = 0

    for line in lines:
        # find difits and their position

        # find digits as digits
        digits = [(position, digit) for position, digit in enumerate(line) if digit.isdigit()]
        
        # find digits as words
        for value, word in enumerate(digit_words):
            index = line.find(word)
            while index != -1:
                digits.append((index, str(value)))
                index = line.find(word, index+1)

        # Get first and last digits
        digits.sort(key=lambda x: x[0])
        line_score = int(digits[0][1] + digits[-1][1])
        #print(f"Line {line} - Digits: {digits}, Line Score: {line_score}")
        score += line_score

    return score


def main(lines: List[str]):
    print(f"Part 1: {compute_part1(lines)}")
    print(f"Part 2: {compute_part2(lines)}")
