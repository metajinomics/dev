#!/usr/bin/python

#this program separate sequences in fasta file to many fasta files
#usage: python separate_fasta.py input.fasta

import sys
filename = sys.argv[1]
i = 0
flag = 0
for line in open(filename,'r'):
    if(line[:1] == ">" and flag == 0):
        i += 1
        flag = 1
        fwrite = open(filename+str(i)+".fa",'w')
        fwrite.write(line)
    elif (line[:1] == ">" and flag == 1):
        i += 1
        fwrite.close()
        fwrite = open(filename+str(i)+".fa",'w')
        fwrite.write(line)
    else:
        fwrite.write(line)
