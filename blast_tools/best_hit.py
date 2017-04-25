#!/usr/bin/python

#usage: python best_hit.py input > output

import sys

prev = ""
for line in open(sys.argv[1],'r'):
    spl = line.strip().split('\t')
    if not prev == spl[0]:
        prev = spl[0]
        print line,
