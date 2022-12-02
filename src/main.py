"""
bla
"""

import importlib
import sys
from helpers import helpers

def main(argv):
    year = argv[0]
    day = argv[1]

    module_name = f"year_{year}.day_{day}.day_{day}"
    print(module_name)
    module = importlib.import_module(module_name)
    module.main(helpers.get_input(year, day))


if __name__ == "__main__":
    main(sys.argv[1:])
