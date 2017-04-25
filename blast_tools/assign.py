#!/usr/bin/python

#usage: python assign.py db.fna best.out > output

import sys

d = {}
cut = float(sys.argv[3])

for line in open(sys.argv[1],'r'):
    if line[:1] == ">":
        spl = line[1:].strip().split(' ')
        d[spl[0]] = spl[1]

for line in open(sys.argv[2],'r'):
    spl = line.strip().split('\t')
    sco = float(spl[2])
    result = []
    for i in range(0,2):
        result.append(spl[i])
    if sco > cut:
        result.append(d[spl[1]])
    else:
        result.append("unassigned")

