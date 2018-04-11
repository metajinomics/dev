#!/usr/bin/python 
"""
This script interleave two fastq into one fastq
usage:
python rarefy_paired_read.py fastq1 fastq2 2
"""

import sys
import random

def main():
    r2 = open(sys.argv[2],'r')
    even_num = int(sys.argv[3])
    r1write = open(sys.argv[1]+'.'+str(even_num)+'.fastq','w')
    r2write = open(sys.argv[2]+'.'+str(even_num)+'.fastq','w')

    num_lines =sum(1 for line in open(sys.argv[1],'r'))

    num_sets = num_lines/4
    ran = random.sample(range(0,num_sets),even_num)

    ran4 = []
    for x in ran:
        ran4.append(x*4+3)


    r1temp = []
    r2temp = []
    for n, r1line in enumerate(open(sys.argv[1],'r')):
        if n % 4 == 3:
            r1temp.append(r1line)
            r2temp.append(r2.readline())
            if n in ran4:
                r1write.write(''.join(r1temp))
                r2write.write(''.join(r2temp))
            r1temp = []
            r2temp = []
        else:
            r1temp.append(r1line)
            r2temp.append(r2.readline())


if __name__ == '__main__':
    main()
