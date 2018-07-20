#!/usr/bin/python 
"""
This script do ...
usage:find sequences hit both R1 and R2
python both_hit.py blast.R1 blast.R2 > output
"""

import sys

def main():
    #read R2 name
    R2 = {}
    for line in open(sys.argv[2],'r'):
        spl = line.strip().split('\t')
        R2[spl[0]] = 0

    #compare R1 then make output
    for line in open(sys.argv[1],'r'):
        spl = line.strip().split('\t')
        if R2.has_key(spl[0]):
            print line,

if __name__ == '__main__':
    main()
