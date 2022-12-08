from pprint import pprint
from typing import List

def analyse_disk(lines):
    directories = {
        '/': 0
    }
    current_path = ['/']
    for line in lines:
        if line == '$ ls' or line.startswith('dir '):
            continue
        if line.startswith('$ cd'):
            splits = line.split(' ')
            if splits[2] == '..':
                current_path.pop()
            elif splits[2] == '/':
                current_path = ['/']
            else:
                current_path.append(splits[2])
        else:
            [size, _] = line.split(' ')
            for index, _ in enumerate(current_path):
                full_path = '/'.join(current_path[:index + 1])
                if full_path in directories:
                    directories[full_path] += int(size)
                else:
                    directories[full_path] = int(size)
    return directories


def compute_part1(lines: List[str]) -> int:
    directories = analyse_disk(lines)
    return sum(value for value in directories.values() if value <= 100_000)


def compute_part2(lines: List[str]) -> int:
    disk_space = 70_000_000
    free_space_needed = 30_000_000
    
    directories = analyse_disk(lines)
    space_to_free = free_space_needed - (disk_space - directories['/']) 

    directories_sorted = sorted(directories.items(), key=lambda item: item[1])
    item = next(item for item in directories_sorted if item[1] >= space_to_free)
    return item[1]



def main(lines: List[str]):
    print(f"Part 1: {compute_part1(lines)}")
    print(f"Part 2: {compute_part2(lines)}")
