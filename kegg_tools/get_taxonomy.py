

import sys
import taxonomy_finder

for line in open(sys.argv[1],'r'):
    spl = line.strip().split('\t')
    tax = taxonomy_finder.get_taxonomy(spl[2])
    print spl[0]+'\t'+ '\t'.join(tax)
