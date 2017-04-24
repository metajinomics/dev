#!/usr/bin/python

#usage: python subset_fasta.py SILVA_128_SSURef_tax_silva.fasta Mycrocystis > Mycrocystis.fa
import sys
flag = 0
for line in open(sys.argv[1],'r'):
    if line[:1] == ">":
        flag = 0
        if sys.argv[2] in line:
            print line,
            flag = 1
            
    else: 
        if flag == 1:
            print line,
    
        
