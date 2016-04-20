#!/usr/bin/python
#usage: python repset_distribution.py repset.fna

import sys

dict = {}
fread = open(sys.argv[1],'r')
for line in fread:
    if (line[:1]==">"):
        continue
    le = len(line.strip())
    if(dict.has_key(le)):
        temp = dict[le]
        dict[le] = temp + 1
    else:
        dict[le] = 1
so = sorted(dict)
total = 0
be = 0
ab = 0
th = 99
for i in so:
    print i,dict[i]
    total = total + dict[i]
    if(dict[i] >= th):
        ab = ab + dict[i]
    else:
        be = be + dict[i]

#print "total",total
#print "threshold",th
#print "above",ab
#print "below",be
