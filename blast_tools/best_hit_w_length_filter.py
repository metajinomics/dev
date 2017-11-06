#!/usr/bin/python

#usage: python best_hit.py input filter> output

import sys

filter = int(sys.argv[2])
prev = ""
for line in open(sys.argv[1],'r'):
    spl = line.strip().split('\t')
    if not prev == spl[0]:
        prev = spl[0]
        if spl[3] > filter:
            print line,
