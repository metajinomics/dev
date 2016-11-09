#!/usr/bin/python

#this script remove list
#usage: python remove_list.py original_list.txt list_to_remove.txt > new_list.txt

import sys

d = {}
for line in open(sys.argv[2],'r'):
    d[line.strip()] = 0

for line in open(sys.argv[1],'r'):
    if not d.has_key(line.strip()):
        print line.strip()
