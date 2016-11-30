#!/usr/bin/python
#this script covert tsv file into fasta file

import sys

for line in open(sys.argv[1],'r'):
    spl = line.strip().split('\t')
    if not spl[2] == "-":
        print ">F:%s_%s\n%s" %(spl[0],spl[1],spl[2])
    if not spl[3] == "-":
        print ">R:%s_%s\n%s" %(spl[0],spl[1],spl[3])

