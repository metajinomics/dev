#!/usr/bin/python
#usage: python 350_to_gtf.py 350 > output

import sys
for line in open(sys.argv[1],'r'):
    if not (line[:1] == ">"):
        continue
    spl = line[1:].strip().split('_')
    le = len(spl)
    ids = line[1:].strip()
    start = spl[le - 3]
    end = spl[le - 2]
    strand = spl[le - 1]
    result = [ids,"coding_region","gene",start,end,".",strand,".","unkown_function"]
    print "\t".join(result)
