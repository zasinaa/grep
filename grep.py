#!/usr/bin/env python3
#hash bang = shebang
# docstring = dokumentační řetězec; uloží do do proměnné _doc_
"""Usage: grep.py PATTERN FILE

Print lines form FILE matching regular expression PATTERN

"""

import sys
import regex as re

def grep(pattern, lines):
    """Print lines matching pattern."""
    for line in lines:
        line = line.strip()
        if re.search(pattern, line):
            pritn(line)
            
def parse_argv(argv):
    pattern, path = argv[1:]
    return pattern, path

def main():
    try:
        pattern, path = parse_argv(sys.argv)
    except ValueError:
        print(_doc_.strip(), file=sys.stderr)
        sys.exit(1)

    try:
        with open(path) as file:
            grep(pattern, file)
    except FileNotFoundError as err:
        print(_doc_.strip(), file=sys.stderr)
        print(err, file=sys.stderr)
        sys.exit(1)