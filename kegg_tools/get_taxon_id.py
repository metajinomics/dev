#!/usr/bin/python

#this script get taxon id from taxonomic_rank file
#usage: python get_taxon_id.py tanomic_rank file > output

import sys

d = {}
for line in open(sys.argv[1],'r'):
    if line[:1] == "#":
        continue
    spl = line.strip().split('\t')
    d[spl[0]]= line.strip()

for line in open(sys.argv[2],'r'):
    ids = line.strip().split(':')
    if d.has_key(ids[0]):
        print '\t'.join([line.strip(), d[ids[0]]])
    else:
        print line.strip()
