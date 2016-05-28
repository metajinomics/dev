#!/usr/bin/python
# this script separate fastq file into samples
#usage: python separate_by_sample.py desciption fastaq 
import sys


def check_barcode(seq,dict):
    if( dict.has_key(seq[1][-12:])):
        print seq[1]

def main():
    dict = {}
    inforead = open(sys.argv[1],'r')
    for line in inforead:
        if (line[:1] == "#"):
            continue
        else:
            spl = line.strip().split('\t')
            dict[spl[3]] = spl[0]

    seqread = open(sys.argv[2],'r')
    seq  = [] 
    for n,line in enumerate(seqread):
        if( n % 4 == 3):
            seq.append(line.strip())
            check_barcode(seq,dict)
            seq = []
        else:
            seq.append(line.strip())


if __name__ == '__main__':
    main()
