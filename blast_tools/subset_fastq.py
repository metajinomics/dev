#!/usr/bin/python

"""
usage:
"""

import sys


def main():
    blastf = sys.argv[1]
    blastr = sys.argv[2]
    fastq = sys.argv[3]

    blaf = {}
    blar = {}
    for line in open(blastf,'r'):
        spl = line.strip().split('\t')
        blaf[spl[0]] = 0
    
    for line in open(blastr,'r'):
        spl = line.strip().split('\t')
        blar[spl[0]] = 0

    flag = 0
    for n,line in enumerate(open(fastq,'r')):
        if n%4 == 0:
            flag = 0
            spl = line[1:].strip().split(' ')
            if blaf.has_key(spl[0]) and blar.has_key(spl[0]):
                flag = 1
                print line,
        else:
            if flag == 1:
                print line,


if __name__ == '__main__':
    main()
