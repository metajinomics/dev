#!/usr/bin/python

"""
usage: python get_map.py genbank_file > output
"""

import sys

def main():
    blast_out_file = sys.argv[1]
    prev = ""
    for line in open(blast_out_file,'r'):
        if prev.split('\t')[0] == line.split('\t')[0]:
            if prev.split('\t')[1].split(':')[1] == line.split('\t')[1].split(':')[1]:
                print prev,
                print line,
            prev = line
        else:
            prev = line
            continue



if __name__ == '__main__':
    main()
