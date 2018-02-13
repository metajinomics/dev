#!/usr/bin/python

"""
This script do ...
usage:
python filename.py arg1...
"""

import sys
from string import maketrans

def get_rc(seq):
    seq = seq.upper()
    trans = maketrans("AGCT","TCGA")
    seq = seq.translate(trans,'xm')
    seq = seq[::-1]
    return seq


def main():
    for n,line in enumerate(open(sys.argv[1],'r')):
        if n%4 == 1:
            print get_rc(line.strip())
            continue
        elif n%4 == 3:
            print line.strip()[::-1]
        print line,


if __name__ == '__main__':
    main()
