#!/usr/bin/env python3
#hash bang = shebang
# docstring = dokumentační řetězec; uloží do do proměnné _doc_
"""Usage: grep.py PATTERN FILE

Print lines form FILE matching regular expression PATTERN

"""

import sys
import regex as re

try:
    pattern, path = sys.argv[1:]
except ValueError:
    print(_doc_.strip(), file=sys.stderr)
    sys.exit(1)
    
try:
    with open(path) as file:
    for line in file:
        line = line.strip("\n")
        if re.search(pattern, line):
            print(line)
except FileNotFoundError as err:
    print(_doc_.strip(), file=sys.stderr)
    print(err, file=sys.stderr)
    sys.exit(1)