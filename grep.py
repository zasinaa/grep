#!/usr/bin/env python3
#hash bang = shebang

import sys

pattern, path = sys.argv[1:]
with open(path) as file:
    for line in file:
        line = line.strip("\n")
        if pattern in line:
            print(line)