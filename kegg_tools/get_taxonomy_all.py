#!/usr/bin/python

#this script will get all taxonomy rank for all kegg organism
#usage: python get_taxonomy_all.py taxonomic_rank > output

import sys
import taxonomy_finder

for line in open(sys.argv[1],'r'):
    if line[:1] == "#":
        continue
    spl = line.strip().split('\t')
    if len(spl) > 2:
        tax = taxonomy_finder.get_taxonomy(spl[2])
    else:
        tax = ["null","null","null","null","null","null","null"]
    #print tax
    print spl[0]+'\t'+ '\t'.join(tax)
