#!/usr/bin/python
#usage: python make_small_mapping.py list64.txt jin_mapping.new.filename.txt > small64_mapping.txt
import sys

list = {}

for line in open(sys.argv[1], 'r'):
    list[line.strip()] = line.strip()

for line in open(sys.argv[2],'r'):
    if(line[:1] == "#"):
        print line.strip()
        continue
    spl = line.strip().split('\t')
    if list.has_key(spl[0]):
        print line.strip()
