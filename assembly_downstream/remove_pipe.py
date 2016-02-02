#!/usr/bin/python

import sys
fread = open(sys.argv[1],'r')
print fread.next()
for line in open(sys.argv[1],'r'):
    spl =  line.strip().split("|")
    if (len(spl) == 2):
        print spl[1]
        
