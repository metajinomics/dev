#!/usr/bin/python

#usage: python best_hit.py input filter> output

import sys

filter = int(sys.argv[2])
iden = float(sys.argv[3])
prev = ""
for line in open(sys.argv[1],'r'):
    spl = line.strip().split('\t')
    if not prev == spl[0]:
        prev = spl[0]
        if int(spl[3]) > filter and float(spl[2]) > iden:
            print line,
