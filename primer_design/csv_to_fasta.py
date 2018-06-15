#!/usr/bin/python 
"""
This script do convert csv file into fasta
usage:
python csv_to_fasta.py csvfile.csv > output.fasta
"""

import sys

def main():
    for n,line in enumerate(open(sys.argv[1],'r')):
        if n == 0:
            continue
        spl = line.strip().split(',')
        print ">F:"+spl[0]
        print spl[1]
        print ">R:"+spl[0]
        print spl[2]




if __name__ == '__main__':
    main()
