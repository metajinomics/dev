#!/usr/bin/python 
"""
This script remove orphans
usage:
python remove_orphans.py R1.fastq R2.fastq
"""

import sys
import gzip


def main():
    R1 = {}
    temp = []

    if (sys.argv[1][-2:] == 'gz'):
        r1read = gzip.open(sys.argv[1],'r')
        r1write = open(sys.argv[1][:-8]+"fix.fastq",'w')
    else:
        r1read = open(sys.argv[1],'r')
        r1write= open(sys.argv[1][:-6]+"fix.fastq",'w')

    for n,line in enumerate(r1read):
        if n % 4 == 3:
            temp.append(line)
            spl = temp[0].split(' ')
            R1[spl[0]] = ''.join(temp)
            temp = []
        else:
            temp.append(line)

    if (sys.argv[2][-2:] == 'gz'):
        r2read = gzip.open(sys.argv[2],'r')
        r2write= open(sys.argv[2][:-8]+"fix.fastq",'w')
    else:
        r2read = open(sys.argv[2],'r')
        r2write= open(sys.argv[2][:-6]+"fix.fastq",'w')

    temp = []

    for n,line in enumerate(r2read):
        if n % 4 == 3:
            temp.append(line)
            spl = temp[0].split(' ')
            if R1.has_key(spl[0]):
                r1write.write(R1[spl[0]])
                r2write.write(''.join(temp))
            temp=[]
        else:
            temp.append(line)
        
if __name__ == '__main__':
    main()
