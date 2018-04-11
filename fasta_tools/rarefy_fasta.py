#!/usr/bin/python 
"""
This script random sampling fasta file
usage:
python rarefy.py fastafile.fasta 3 > output.fasta
"""

import sys
import random

def main():
    #get number of line
    even_num = int(sys.argv[2])
    num_lines = sum(1 for line in open(sys.argv[1],'r'))

    num_sets = num_lines/2
    ran = random.sample(range(0,num_sets),even_num)

    ran4 = []
    for x in ran:
        ran4.append(x*2+1)

    temp = []
    for n, line in enumerate(open(sys.argv[1],'r')):
        if n % 2 == 1:
            temp.append(line)
            if n in ran4:
                print ''.join(temp),
            temp = []
        else:
            temp.append(line)
if __name__ == '__main__':
    main()
