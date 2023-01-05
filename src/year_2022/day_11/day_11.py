from dataclasses import dataclass, field
from typing import List, Optional
from pprint import pprint
import math

@dataclass
class Monkey:
    items: Optional[List[str]] = field(default_factory=list)
    operator: Optional[str] = '+'
    operation_operand: Optional[str] = '0'
    test_operand: Optional[int] = 0
    target_if_true: Optional[int] = 0
    target_if_false: Optional[int] = 0
    inspected_items_count: int = 0


def analyse_input(lines: List[str]) -> List[Monkey]:
    monkeys = []
    for line in lines:
        if line.startswith("Monkey"):
            monkeys.append(Monkey())
        elif line.startswith('  Starting'):
            monkeys[-1].items = [int(item) for item in line.split(': ')[1].split(', ')]
        elif line.startswith('  Operation'):
            monkeys[-1].operator = line.split(' ')[-2]
            monkeys[-1].operation_operand = line.split(' ')[-1]
        elif line.startswith('  Test'):
            monkeys[-1].test_operand = int(line.split(' by ')[-1])
        elif line.startswith('    If true'):
            monkeys[-1].target_if_true = int(line.split(' monkey ')[1])
        elif line.startswith('    If false'):
            monkeys[-1].target_if_false = int(line.split(' monkey ')[1])
    return monkeys


def compute_part1(lines: List[str]) -> int:
    monkeys = analyse_input(lines)
    pprint(monkeys)

    modulo = math.prod([monkey.test_operand for monkey in monkeys])

    for i in range(10000):
        for monkey in monkeys:
            if i == 206:
                print(f"monkey has {len(monkey.items)} items")
            while monkey.items:
                item = monkey.items.pop(0)
                # worry increse
                if monkey.operator == '+':
                    item = item + (int(monkey.operation_operand) if monkey.operation_operand.isdigit() else item)
                elif monkey.operator == '*':
                    item = item * (int(monkey.operation_operand) if monkey.operation_operand.isdigit() else item)
                if i == 206:
                    print("operation done")
                # worry relief
                item = item % modulo
                # test
                if item % monkey.test_operand == 0:
                    monkeys[monkey.target_if_true].items.append(item)
                    if i == 206:
                        print(f"item is true")
                else:
                    monkeys[monkey.target_if_false].items.append(item)
                    if i == 206:
                        print(f"item is false")

                monkey.inspected_items_count += 1
        print(i)


    item_counts_sorted = sorted([monkey.inspected_items_count for monkey in monkeys], reverse=True)
    print(item_counts_sorted)
    return math.prod(item_counts_sorted[:2])


def compute_part2(lines: List[str]) -> int:
    score = 0
    return score


def main(lines: List[str]):
    print(f"Part 1: {compute_part1(lines)}")
    print(f"Part 2: {compute_part2(lines)}")
