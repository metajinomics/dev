#!/usr/bin/python 
"""
This script interleave two fasta into one fasta
usage:
python rarefy_paired_read.py fasta1 fasta2 2 > output.interleaved.fasta
"""

import sys
import random

def main():
    r2 = open(sys.argv[2],'r')
    even_num = int(sys.argv[3])

    num_lines =sum(1 for line in open(sys.argv[1],'r'))

    num_sets = num_lines/2
    ran = random.sample(range(0,num_sets),even_num)

    ran4 = {}
    for x in ran:
        ran4[x*2+1] = 0


    r1temp = []
    r2temp = []
    for n, r1line in enumerate(open(sys.argv[1],'r')):
        if n % 2 == 1:
            r1temp.append(r1line)
            r2temp.append(r2.readline())
            if ran4.has_key(n):
                print ''.join(r1temp),
                print ''.join(r2temp),
            r1temp = []
            r2temp = []
        else:
            r1temp.append(r1line)
            r2temp.append(r2.readline())


if __name__ == '__main__':
    main()
