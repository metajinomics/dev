#!/usr/bin/python
#usage: python print_len_fasta.py fastafile
import sys
flag = 0
length = 0
seq = []
name = ""
for line in open(sys.argv[1],'r'):
    if (flag == 0 and line[:1]==">"):
        name = line.strip()
        flag = 1
        continue
    elif (flag == 1 and line[:1]==">"):
        temp = ''.join(seq)
        print len(temp)
        #if( len(temp)> 500 and len(temp) < 2000):
        #    print name
        #    print temp
        seq = []
        name = line.strip()
    else:
        seq.append(line.strip())

temp = ''.join(seq)
print len(temp)
#if( len(temp)> 500 and len(temp) < 2000):
#    print name
#    print temp
        
