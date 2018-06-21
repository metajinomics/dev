#!/usr/bin/python 
"""
This script do ...
usage:
python filename.py arg1...
"""

import sys
import screed

def main():

    li = {}
    for line in open(sys.argv[1],'r'):
        li[line.strip()] = 0

    for record in screed.open(sys.argv[2]):
        if not li.has_key(record.name):
            print ">"+record.name + '\n' + record.sequence

if __name__ == '__main__':
    main()
