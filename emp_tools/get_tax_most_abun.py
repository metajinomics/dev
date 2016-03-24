#!/usr/bin/python
import sys

dict = {}
for line in open(sys.argv[1],'r'):
    spl = line.strip().split(':')
    dict[spl[0]]=line.strip()

for line in open(sys.argv[2],'r'):
    spl = line.strip().split('\t')
    if (dict.has_key(spl[0])):
        out= [dict[spl[0]],line.strip()]
        print '\t'.join(out)
