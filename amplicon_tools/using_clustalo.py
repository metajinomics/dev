#!/usr/bin/python 
"""
This script do ...
usage:
python find_center_seq.py list fasta
"""

import sys
import screed

def main():
    #read fasta
    

    #read list
    li = []
    otus = []
    seq_list = []
    for n,line in enumerate(open(sys.argv[1],'r')):    
        spl = line.strip().split('\t')
        if n == 0:
            otus = spl
        elif n == 1:
            seq_list = spl
        else:
            continue


    #find represent
    for i in range(2,len(otus)):
        li = seq_list[i].split(',')
        if len(li) > 2:

            print otus[i], li

    

if __name__ == '__main__':
    main()
