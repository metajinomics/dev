#!/usr/bin/python 
"""
This script interleave two fastq into one fastq
usage:
python interleave.py fastq1 fastq2 > output
"""

import sys

def main():
    r2 = open(sys.argv[2],'r')
    r1temp = []
    r2temp = []
    for n, r1line in enumerate(open(sys.argv[1],'r')):
        if n % 4 == 3:
            r1temp.append(r1line)
            r2temp.append(r2.readline())
            print ''.join(r1temp),
            print ''.join(r2temp),
            r1temp = []
            r2temp = []
        else:
            r1temp.append(r1line)
            r2temp.append(r2.readline())


if __name__ == '__main__':
    main()
