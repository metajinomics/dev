#!/usr/bin/python
#usage: pthon remove_dot_fasta.py inpufile
#example: python remove_dot_fasta.py refsoil_bac_ali.afa > refsoil_bac_ali_name.afa
import sys

for line in open(sys.argv[1]):
    if(line[:1]==">"):
        print line.strip().split('.')[0]
    else:
        print line.strip()
