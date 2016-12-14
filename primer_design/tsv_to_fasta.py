#!/usr/bin/python
#this script covert tsv file into fasta file

import sys

for line in open(sys.argv[1],'r'):
    if line.strip() == "target_gene\ttarget_locus\tF_trad\tR_trad\tProduct_length":
        continue
    spl = line.strip().split('\t')
    if spl[2] != "-" and spl[2] != "_":
        print ">F:%s_%s\n%s" %(spl[0],spl[1],spl[2])
    if spl[3] != "-" and spl[3] != "_":
        print ">R:%s_%s\n%s" %(spl[0],spl[1],spl[3])

