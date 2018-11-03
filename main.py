import sys
import os
import textwrap

from shutil import copy
from pathlib import Path

def try_else(a, b):
    try:
        return a()
    except:
        return b()

def print_usage():
    print(textwrap.dedent(main.__doc__)[1:-1])

def main():
    """
    Usage:

        FROM=src TO=dest wcp files...

    Copies files in `src` into `dest`, without needing to repeat the directory name.

    Environment variables FROM and TO define the source and destination
    directories respectively. Both default to the current directory. For each
    file in `src` that is specified in an argument, copies that file into `dest`.
    """

    if len(sys.argv) == 1:
        print_usage()
        exit(1)

    FROM = Path(try_else(lambda: os.environ["FROM"], lambda: ""))
    TO =   Path(try_else(lambda: os.environ["TO"]  , lambda: ""))

    for arg in sys.argv[1:]:
        copy(FROM / arg, TO)

if __name__ == "__main__":
    main()

