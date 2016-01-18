#!/usr/bin/python
#usage: pthon replace_dot_fasta.py inpufile
#example: python replace_dot_fasta.py refsoil_bac_ali.afa > refsoil_bac_ali_name.afa
import sys

for line in open(sys.argv[1]):
    if(line[:1]==">"):
        print line.strip().split('.')[0]+'_'+line.strip().split('.')[1].split(' ')[0]
    else:
        print line.strip()
