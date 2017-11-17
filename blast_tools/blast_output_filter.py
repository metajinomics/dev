#!/usr/bin/python

"""
usage: blast_output_filter.py databasefile blastoutput identity lengh > output
"""

import sys
import screed

def main():
    #read db file
    db = {}
    fasta_file = sys.argv[1]
    for record in screed.open(fasta_file):
        db[record.name.split(' ')[0]] = len(record.sequence)

    blast_file = sys.argv[2]
    iden_filter = float(sys.argv[3])
    len_filter = float(sys.argv[4])

    prev = ""
    for line in open(blast_file,'r'):
        spl = line.strip().split('\t')
        if len(spl) < 3:
            continue

        if not prev == spl[0]:
            percent = (int(spl[3]) / db[spl[1]]) * 100
            if float(spl[2]) > idenfilter and percent > len_filter:  
                print line,
            prev = spl[0]


if __name__ == '__main__':
    main()
