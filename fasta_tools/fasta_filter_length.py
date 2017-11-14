#!/usr/bin/python

"""

usage: python fasta_filter_length.py fasta_file length > filtered.fa

"""
import sys
import screed



def main():
    filter_length = int(sys.argv[2])
    for record in screed.open(sys.argv[1]):
        if len(record.sequence) > filter_length:
            print ">" + record.name + '\n' + record.sequence

if __name__ == '__main__':
    main()
