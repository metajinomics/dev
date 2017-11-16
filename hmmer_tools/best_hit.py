#!/usr/bin/python

"""

usage: python best_hit.py hmmscan_result > output
"""

import sys

def main():
    prev = ""
    for line in open(sys.argv[1],'r'):
        if line[:1] == "#":
            continue
        spl = line.strip().split('\t')
        if not prev == spl[2]:
            print line,
            prev = spl[2]

if __name__ == '__main__':
    main()
