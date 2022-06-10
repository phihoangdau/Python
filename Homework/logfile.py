#!/usr/bin/env python3
import sys
import re
# sys.argv is a list in Python that contains all the command-line arguments passed to the script.
logfile = sys.argv[1]
with open(logfile) as f:
    for line in f:
        if "[crit]" not in line:
            continue
        else:
            print(line.strip())