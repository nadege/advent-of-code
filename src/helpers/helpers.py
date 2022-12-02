"""
Helpers functions
"""

from typing import List


def get_input(year, day: int)-> List[str]:
    """
    Read the input for the day
    """

    with open(f"src/year_{year}/day_{day}/input.txt") as file:
        return file.read().splitlines()
