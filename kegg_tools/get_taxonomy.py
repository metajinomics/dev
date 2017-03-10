#!/usr/bin/python
#this script get full taxonomy from NCBI

import sys
import taxonomy_finder
import time
for line in open(sys.argv[1],'r'):
    spl = line.strip().split('\t')
    if len(spl) > 2:
        tax = taxonomy_finder.get_taxonomy(spl[2])
    else:
        tax = ["null","null","null","null","null","null","null"]
    #print tax
    print spl[0]+'\t'+ '\t'.join(tax)
    time.sleep(1.0/3)
