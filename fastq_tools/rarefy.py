#!/usr/bin/python 
"""
This script random sampling fastq file
usage:
python rarefy.py fastqfile.fastq 3 > output.fastq
"""

import sys
import random

def main():
    #get number of line
    even_num = int(sys.argv[2])
    num_lines = sum(1 for line in open(sys.argv[1],'r'))

    num_sets = num_lines/4
    ran = random.sample(range(0,num_sets),even_num)

    ran4 = {}
    for x in ran:
        ran4[x*4+3] = 0

    temp = []
    for n, line in enumerate(open(sys.argv[1],'r')):
        if n % 4 == 3:
            temp.append(line)
            if ran4.has_key(n):
                print ''.join(temp),
            temp = []
        else:
            temp.append(line)
if __name__ == '__main__':
    main()
