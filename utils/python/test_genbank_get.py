#!/usr/bin/python
import sys
sys.path.append('./utils')
import genbank_get

filename = sys.argv[1]
organism = genbank_get.organism(filename)
print filename + '\t' + organism

taxon = genbank_get.taxon(filename)
print filename + '\t' + taxon
